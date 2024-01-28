import asyncio
import zipfile
from io import BytesIO
from urllib.parse import urljoin
from striprtf.striprtf import rtf_to_text
from PIL import Image
from httpx import AsyncClient
from fuzzywuzzy import fuzz


class NoText(Exception):
    pass


APP_ID = "5fadf8c3-326a-4a0b-a8a6-1e403beb5605"
APP_PASS = "/D38wqEHqX+OJ9UbGaxH5XwO"
PROCESSING_URL = "https://cloud-westus.ocrsdk.com"


async def content_generator(data):
    yield data


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


async def compress_img(image_data: bytes, new_size_ratio: float = 0.9, quality: int = 90, width=None,
                       height=None):
    img_file = BytesIO()
    img_file.write(image_data)
    img = Image.open(img_file)
    if new_size_ratio < 1.0:
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)
    elif width and height:
        img = img.resize((width, height), Image.LANCZOS)
    new_io = BytesIO()
    try:
        new_io.name = "result.jpg"
        img.save(new_io, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        new_io.name = "result.jpg"
        img.save(new_io, quality=quality, optimize=True)
    return new_io


class FineReader:
    def __init__(self):
        self.session = AsyncClient()
        self.session.auth = (APP_ID, APP_PASS)

    async def extractText(self, image_data):
        url = urljoin(PROCESSING_URL, "v2/processImage")
        req = await self.session.post(url, params={
            "imageSource": "auto",
            "language": "English,German,Russian",
            "profile": "textExtraction",
            "exportFormat": "rtf,xml",
            "textType": "normal,typewriter,matrix,index,index,handprinted,ocrA,ocrB,gothic"
        }, data=image_data, timeout=10000)
        new_r_json = req.json()
        new_task_id = new_r_json.get("taskId")
        n_url = None
        if new_task_id:
            conf_url = urljoin(PROCESSING_URL, "v2/getTaskStatus")
            while True:
                suc_req = await self.session.get(conf_url, params={
                    "taskId": new_task_id
                })
                suc_json = suc_req.json()
                status = suc_json.get("status")
                if status:
                    if status == "Completed":
                        urls = suc_json["resultUrls"]
                        n_url = urls[0]
                        break
                    else:
                        await asyncio.sleep(0.25)
                        continue
                else:
                    await asyncio.sleep(0.25)
                    continue
        if n_url:
            s = AsyncClient()
            rtf_data_req = await s.get(n_url)
            rtf_data_read = rtf_data_req.read()
            rtf_data = rtf_data_req.read().decode("utf-8")
            text_content = rtf_to_text(rtf_data)
            s_text_content = text_content.strip()
            if not s_text_content:
                raise NoText
            else:
                return s_text_content, rtf_data_read

    async def processImage(self, image_data, level: int = 0, res_change: bool = False, add_rft: bool = False):
        url = urljoin(PROCESSING_URL, "v2/processImage")
        req = await self.session.post(url, params={
            "imageSource": "auto",
            "language": "English,German,Russian",
            "profile": "documentConversion",
            "exportFormat": "rtf,xml",
            "textType": "normal,typewriter,matrix,index,index,handprinted,ocrA,ocrB,gothic"
        }, data=image_data, timeout=10000)
        r_json = req.json()
        task_id = r_json.get("taskId")
        n_url = None
        if task_id:
            conf_url = urljoin(PROCESSING_URL, "v2/getTaskStatus")
            while True:
                suc_req = await self.session.get(conf_url, params={
                    "taskId": task_id
                })
                suc_json = suc_req.json()
                status = suc_json.get("status")
                if status:
                    if status == "Completed":
                        urls = suc_json["resultUrls"]
                        n_url = urls[0]
                        break
                    else:
                        await asyncio.sleep(0.25)
                        continue
                else:
                    await asyncio.sleep(0.25)
                    continue
        if n_url:
            s = AsyncClient()
            rtf_data_req = await s.get(n_url)
            rtf_data = rtf_data_req.read().decode("utf-8")
            text_content = rtf_to_text(rtf_data)
            s_text_content = text_content.strip()
            if not s_text_content:
                raise NoText
            else:
                start_text = (await self.extractText(image_data))[0]
                dat = image_data
                if res_change:
                    new_res = 0.99
                    quality = 75
                else:
                    new_res = 1
                    quality = 69
                cur_level = 0
                if level == 0:
                    n_levels = None
                else:
                    n_levels = level
                while True:
                    if n_levels:
                        if cur_level >= n_levels:
                            break
                    new_image = await compress_img(dat, new_size_ratio=new_res, quality=quality)
                    new_image_data = new_image.getvalue()
                    extracted = await self.extractText(new_image_data)
                    rtf_data = extracted[1]
                    new_text = extracted[0] or ""

                    dat = new_image_data
                    procent = fuzz.ratio(start_text.strip().lower(), new_text.strip().lower())
                    if not n_levels:
                        if procent <= 98:
                            break
                    if res_change:
                        quality -= 17
                    else:
                        quality -= 35
                    if quality < 1:
                        quality = 1
                    cur_level += 1
                if add_rft:
                    final_io = BytesIO()
                    with zipfile.ZipFile(final_io, "a",
                                         zipfile.ZIP_DEFLATED, compresslevel=9, allowZip64=True) as zip_file:
                        for file_name, data in [('result.jpg', dat),
                                                ('result.rtf', rtf_data)]:
                            zip_file.writestr(file_name, data)
                    final_io.name = "result.zip"
                    return final_io
                else:
                    final_io = BytesIO()
                    final_io.name = "result.jpg"
                    final_io.write(dat)
                    return final_io


async def main():
    ca = FineReader()
    data = open('../img.png', 'rb').read()
    await ca.processImage(data, add_rft=True)


if __name__ == '__main__':
    asyncio.run(main())
