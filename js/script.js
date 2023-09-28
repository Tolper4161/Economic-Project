const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileList = document.getElementById('file-list');
const resetButton = document.getElementById('reset-button');

function isImage(file) {
    return file.type.startsWith('image/');
}

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('drag-over');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('drag-over');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('drag-over');

    const files = e.dataTransfer.files;

    for (const file of files) {
        if (isImage(file)) {
            const listItem = document.createElement('div');
            listItem.innerText = file.name;
            fileList.appendChild(listItem);
        } else {
            alert('Выбранный файл не является изображением.');
        }
    }
});

fileInput.addEventListener('change', () => {
    const files = fileInput.files;

    for (const file of files) {
        if (isImage(file)) {
            const listItem = document.createElement('div');
            listItem.innerText = file.name;
            fileList.appendChild(listItem);
        } else {
            alert('Выбранный файл не является изображением.');
        }
    }
});

resetButton.addEventListener('click', () => {
    fileList.innerHTML = '';
    fileInput.value = '';
});
