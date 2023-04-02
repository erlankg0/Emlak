// плавное затемнение фона header при скролле
$(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll >= 10) {
        $(".header").addClass("header--scroll");

    } else {
        $(".header").removeClass("header--scroll");
    }
});


const buttons = document.querySelectorAll('.button-with-image');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        buttons.forEach(btn => {
            btn.classList.remove('clicked');
        });
        button.classList.add('clicked');
    });
});


// toggle
const checkbox = document.querySelector('.theme');
const root = document.documentElement;

checkbox.addEventListener('change', function () {
    if (this.checked) {
        root.style.setProperty('--color-primary', '#333333');
        localStorage.setItem('theme', 'dark');
    } else {
        root.style.setProperty('--color-primary', '#1E1E1E');
        localStorage.setItem('theme', 'light');
    }
});

// Проверяем сохраненную тему при загрузке страницы
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    checkbox.checked = true;
    root.style.setProperty('--color-primary', '#333333');
} else {
    checkbox.checked = false;
    root.style.setProperty('--color-primary', '#1E1E1E');
}


function addLike(postId) {
    $.post('/add_like/' + postId + '/', function (data) {
        if (data.status === 'ok') {
            alert('Post liked!');
        } else {
            alert(data.message);
        }
    });
}

function addDislike(postId) {
    $.post('/add_dislike/' + postId + '/', function (data) {
        if (data.status === 'ok') {
            alert('Post disliked!');
        } else {
            alert(data.message);
        }
    });
}

function addFavorite(postId) {
    $.post('/add_favorite/' + postId + '/', function (data) {
        if (data.status === 'ok') {
            alert('Post added to favorites!');
        } else {
            alert(data.message);
        }
    });
}

// топ, новые, горяшие предложения

/*$(document).ready(function () {
    // Загрузка всех объявлений при загрузке страницы
    loadProducts('');

    // Обработка нажатий на кнопки
    $('#top-offers').click(function () {
        loadProducts({type: 'top'});
    });
    $('#new-offers').click(function () {
        loadProducts({type: 'new'});
    });
    $('#hot-deals').click(function () {
        loadProducts({type: 'hot'});
    });
});

function loadProducts(params) {
    // Отправка AJAX-запроса на сервер для получения списка объявлений с заданными параметрами
    $.ajax({
        url: '/api/products/',
        type: 'GET',
        data: params,
        dataType: 'json',
        success: function (response) {
            // Обновление содержимого списка объявлений на странице
            var productsList = $('#products-list');
            productsList.empty(); // Очистка списка
            for (var i = 0; i < response.products.length; i++) {
                var product = response.products[i];
                // Создание HTML-элемента для нового объявления
                var productItem = $('<div class="product-item">' +
                    '<h2>' + product.title + '</h2>' +
                    '<p>' + product.description + '</p>' +
                    '<p>Price: ' + product.price + '</p>' +
                    '<p>Square: ' + product.square + '</p>' +
                    '</div>');
                productsList.append(productItem); // Добавление нового элемента в список
            }
        },
        error: function (xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}
*/

const videoUrl = '/static/video/main.mp4';
const cacheName = 'my-video-cache';

// Проверяем, есть ли файл в кэше
if ('caches' in window) {
    caches.match(videoUrl).then(function (response) {
        if (response) {
            // Используем файл из кэша
            const video = document.querySelector('video');
            video.src = URL.createObjectURL(response);
        } else {
            // Загружаем файл с сервера и сохраняем его в кэше
            fetch(videoUrl).then(function (response) {
                caches.open(cacheName).then(function (cache) {
                    cache.put(videoUrl, response.clone());
                });
                const video = document.querySelector('video');
                video.src = URL.createObjectURL(response);
            });
        }
    });
} else {
    // Кэширование не поддерживается, загружаем файл с сервера
    const video = document.querySelector('video');
    video.src = videoUrl;
}
