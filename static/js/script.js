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
    $.post('/ru/add_like/' + postId + '/', function (data) {
        if (data.status === 'ok') {
            alert('Post liked!');
        } else {
            alert(data.message);
        }
    });
}

function addDislike(postId) {
    $.post('/ru/add_dislike/' + postId + '/', function (data) {
        if (data.status === 'ok') {
            alert('Post disliked!');
        } else {
            alert(data.message);
        }
    });
}

function addFavorite(postId) {
    $.post('/ru/add_favorite/' + postId + '/', function (data) {
        if (data.status === 'ok') {
            alert('Post added to favorites!');
        } else {
            alert(data.message);
        }
    });
}