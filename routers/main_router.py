from typing import Annotated
from fastapi import APIRouter, UploadFile, Form
from starlette.responses import Response, JSONResponse

from fineapi import FineReader, NoText

router = APIRouter()

reader = FineReader()


@router.post("/process")
async def handler(add_rft: Annotated[bool, Form()], res_change: Annotated[bool, Form()],
                  file: Annotated[UploadFile, Form()]):
    filename = file.filename
    file_image = filename.lower().endswith(('.png', '.jpg', '.jpeg'))
    if file_image:
        image_data = await file.read()
        try:
            output = await reader.processImage(image_data, add_rft=add_rft, res_change=res_change, level=0)
        except NoText:
            return JSONResponse(status_code=401, content={
                "error": "На изображении нет текста"
            })
        except:
            return JSONResponse(status_code=401, content={
                "error": "Произошла ошибка"
            })
        if not output:
            return JSONResponse(status_code=401, content={
                "error": "Произошла ошибка"
            })
        filename = output.name
        data = output.getvalue()
        resp = Response(content=data, status_code=200, media_type="application/actet-stream", headers={
            f'Content-Disposition': f'inline; filename="{filename}"'
        })
        return resp
    else:
        return JSONResponse(status_code=401, content={
            "error": "Файл должен быть с расширениями .png или .jpg"
        })
