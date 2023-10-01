<script setup>
import FileForm from './components/FileForm.vue';
// import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header id="header">
  <nav id="top-navbar">
      <h1 id="h1-title">TextImageSqueeze</h1>
      <div class="top-navbar-links desktop">
          <a href="#advantages-link">Преимущества сервиса</a>
          <a href="#about-project">О проекте</a>
          <a href="#footer">Контакты</a>
      </div>
      <div class="mobile top-navbar-mobile-links">
          <button id="menu" class="icon"></button>
      </div>
  </nav>
</header>
<section id="image-loader">
  <div class="container">
      <FileForm />
  </div>
</section>
<div id="advantages-link"></div>
<section id="advantages" class="angles">
  <div class="container">
      <div class="advantages-title-block">
          <h2 class="advantages-title line">Преимущества сервиса</h2>
      </div>
      <div class="advantages-content">
          <div class="advantages-card">
              <img class="icon" src="/template/img/brain.png" alt="">
              <p class="advantages-big-text">Для распознавания текста на изображениях используется ОКР, далее происходит максимально возможное сжатие картинок. После проделанных операций, можно скачать zip-архив с оптимизированными файлами. Современный подход к основной задаче нашего сайта позволяет выполнять работу быстро эффективно.</p>
              <p class="advantages-small-text">Для распознавания текста на изображениях используется ОКР, далее происходит максимально возможное сжатие картинок. После проделанных операций, можно скачать zip-архив с оптимизированными файлами.</p>
          </div>
          <div class="advantages-card">
              <img class="icon" src="/template/img/time-management.png" alt="">
              <p class="advantages-big-text">Нейросеть, используемая сайтом, достаточно обучена, чтобы обработка изображений занимала оптимальное количество времени. Переобучение нейронной сети наоборот, замедлило бы данный процесс. Кроме того, все функции сайта, связанные с данной задачей, максимально оптимизированы, что также способствует ускорению работы. </p>
              <p class="advantages-small-text">Нейросеть, используемая сайтом, достаточно обучена, чтобы обработка изображений занимала оптимальное количество времени. Все функции, связанные с данной задачей, оптимизированы, что также способствует ускорению работы.</p>
          </div>
          <div class="advantages-card">
              <img class="icon" src="/template/img/pendrive.png" alt="">
              <p class="advantages-big-text">Сжатие изображений происходит циклично (число циклов определяется нейросетью автоматически), пока погрешность сжатия не окажется ниже 2%. Данный подход позволяет получать файлы, занимающие гораздо меньше памяти. Кроме того, наш сайт позволяет преобразовывать изображения к документам с расширением .rtf (Rich Text Format).</p>
              <p class="advantages-small-text">Сжатие изображений происходит циклично, пока погрешность не станет ниже 2%, что позволяет получать файлы, занимающие меньше памяти. Также можно преобразовать файлы к документам с расширением .rtf.</p>
          </div>
      </div>
  </div>
</section>
<section id="about-project">
  <div class="container">
      <div class="about-left-col">
          <h2 class="about-left-col-title">О проекте</h2>
          <p class="line-text">К настоящему моменту в мире накоплены большие объемы текстовых неоцифрованных данных. Представляется желанным оцифровывать большое количество информации, которая имеется в виде изображений с текстом. Ввиду того, что получение изображений и распознавание текста являются разными по уровню и требованию задачами, возникает промежуточная проблема - хранение большого количества изображений с текстом, для его дальнейшего распознавания, в сжатом виде с целью экономии места.
            <br>Сайт создан с целью решения данных проблем. Созданное нашей командой API использует нейронную сеть - данное решение наиболее современное и гибкое. Таким образом, происходит сжатие изображений с текстом без потери информации.</p>
      </div>
      <div class="about-right-col">
          <div class="line-img"></div>
      </div>
  </div>
</section>
<footer id="footer">
  <div class="container">
      <div class="footer-links line-text">
          <div class="footer-links-left">
              <div class="footer-col">
                  <h3>Социальные сети</h3>
                  <a>Whatsapp</a>
                  <a>Vkontakte</a>
                  <a>Telegram</a>
                  <a>Discord</a>
              </div>
              <div class="footer-col">
                  <h3>Навигация по сайту</h3>
                  <a>Сжать изображения</a>
                  <a>Преимущества сервиса</a>
                  <a>О проекте</a>
                  <a>Контакты</a>
              </div>
          </div>
          <div class="footer-links-right">
              <div class="footer-col">
                  <h3>Lorem ipsum</h3>
                  <a>Dolor sit amet</a>
                  <a>Consectetur adipiscing </a>
                  <a>Elit sed do </a>
                  <a>Eiusmod tempor</a>
              </div>
              <div class="footer-col">
                  <h3>Помощь</h3>
                  <a>Сайт завис</a>
                  <a>Кнопка "скачать" не работает</a>
                  <a>Изображения не сжимаются</a>
                  <a>Техподдержка</a>
              </div>
          </div>
      </div>
      <div class="footer-social-media">
          <a href="#" id="whatsapp" class="min-icon"></a>
          <a href="#" id="vk" class="min-icon"></a>
          <a href="#" id="telegram" class="min-icon"></a>
          <a href="#" id="discord" class="min-icon"></a>
      </div>
      <h4 class="footer-created-by">Создано командой "Кибер-Викинги"</h4>
  </div>
</footer>
</template>


