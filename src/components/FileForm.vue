<script setup lang="ts">
import { ref } from 'vue'
import axios from "axios"

const state = ref({
  file: undefined,
  rtf_add: false,
  change_res: false,
  errors: [],
  is_loading: false,
  disabled: false
})

const sendForm = async () => {
    const form = new FormData()
    form.append("file", state.value.file)
    form.append("add_rft", state.value.rtf_add)
    form.append("res_change", state.value.change_res)
    state.value.is_loading = true
    state.value.disabled = true
    const req = await axios(
        "http://localhost:8080/process", {
            method: "POST",
            headers: {
                "Accept": "*"
            },
            data: form,
            responseType: 'blob'

        }
    ).then(response => {
        if (response.status == 200) {
            const data = response.data
            var blob = new Blob([data], {type: 'application/actet-stream'});
            const headers = response.headers
            var contentDisposition = headers['content-disposition'];
            var patt = new RegExp('filename="([^;]+\\.[^\\.;]+)"');
            var result = patt.exec(contentDisposition);
            var filename = result[1];
            var downloadElement = document.createElement('a');
            var href = window.URL.createObjectURL(blob);
            downloadElement.style.display = 'none';
            downloadElement.href = href;
            downloadElement.download =filename;
            document.body.appendChild(downloadElement);
            downloadElement.click();
            document.body.removeChild(downloadElement);
            window.URL.revokeObjectURL(href)
            clear()
        }
        
        
    }).catch(async error => {
        const resp = error.response
        if (resp.status == 401) {
            const data = resp.data
            console.log(await data.text())
            let json = JSON.parse(await data.text());
            console.log(json)
            if (json.error) {
                state.value.errors.push(json.error)
                clear()
            }
        }
      }).finally(() => {
        state.value.is_loading = false
        state.value.disabled = false
      }
        
      )
}

const clear = async () => {
    state.value.file = undefined
    const file = document.querySelector('input#drop-zone');
    file.value = null;
    state.value.rtf_add = false
    state.value.change_res = false
}
</script>

<template>
    <form @submit.prevent>
                <div id="image-input-group">
                    <input @input="state.file = $event.target.files[0]" type="file" id="drop-zone" v-bind:class="state.file ? 'drop-zone-active' : 'drop-zone'" accept="image/*">
                    <b v-if="!state.file">Перетащите сюда изображения для сжатия или выберите их самостоятельно,<br class="br-off">кликнув сюда. Чтобы скачать сжатые файлы в виде zip-архива, нажмите<br class="br-off">на кнопку "скачать". Если вы хотите заново загрузить изображения,<br class="br-off">нажмите на кнопку "очистить", чтобы заново выбрать файлы.</b>
                    <b v-else>Изображение загружено<br class="br-off">{{ state.file.name }}</b>
                    <div v-bind:class="!state.is_loading ? 'unactive': ''" class="loading-block">
                        <span class="loader"></span>
                    </div>
                </div>

                <div class="image-loader-options-group">
                    <input type="checkbox" id="CBSmallerQualityImage" name="CBSmallerQualityImage" value="CBSmallerQualityImage" checked v-model="state.change_res">
                    <label for="CBSmallerQualityImage">Уменьшить разрешение изображения</label>
                    <input type="checkbox" id="CBAddrtf" name="CBAddrtf" value="CBAddrtf" checked v-model="state.rtf_add">
                    <label for="CBAddrtf">Преобразовать к rtf</label>
                </div>

                <div class="image-loader-btn-group">
                    <button id="download-button" class="animated-button" :disabled="!state.file || state.disabled" @click="sendForm">Скачать</button>
                    <button id="reset-button" class="animated-button" :disabled="!state.file || state.disabled" @click="clear">Сброс</button>
                </div>
                <p v-for="error in state.errors" id="error-line"> {{ error }}</p>
            </form>
</template>