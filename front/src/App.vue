<script setup>
import FileForm from './components/FileForm.vue';
// import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header id="header">
  <nav id="top-navbar">
      <h1 id="h1-title">ТекстоСховище</h1>
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
          <h2 class="advantages-title line">Преимущества</h2>
      </div>
      <div class="advantages-content">
          <div class="advantages-card">
              <img class="icon" src="/template/img/brain.png" alt="">
              <p class="advantages-big-text">Для распознавания текста на изображениях используется ОКР, далее происходит максимально возможное сжатие картинок. После проделанных операций, можно скачать zip-архив с оптимизированными файлами. Современный подход к основной задаче нашего сайта позволяет выполнять работу быстро эффективно.</p>
              <p class="advantages-small-text">Для распознавания текста на изображениях используется ОКР, далее происходит максимально возможное сжатие картинок. После проделанных операций, можно скачать zip-архив с оптимизированными файлами.</p>
          </div>
          <div class="advantages-card">
              <img class="icon" src="/template/img/time-management.png" alt="">
              <p class="advantages-big-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident...</p>
              <p class="advantages-small-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
          </div>
          <div class="advantages-card">
              <img class="icon" src="/template/img/pendrive.png" alt="">
              <p class="advantages-big-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident...</p>
              <p class="advantages-small-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
          </div>
      </div>
  </div>
</section>
<section id="about-project">
  <div class="container">
      <div class="about-left-col">
          <h2 class="about-left-col-title">Lorem ipsum dolor?</h2>
          <p class="line-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. </p>
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
                  <a>Telegramm</a>
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
                  <a>Elit sed do </a>
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
      <h4 class="footer-created-by">Created by Lorem Ipsum</h4>
  </div>
</footer>
</template>


