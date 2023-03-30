function initSliders() {
    const sliders = document.querySelectorAll('.slider');
    sliders.forEach(slider => {
        // инициализация слайдера
        const sliderId = slider.getAttribute('id');
        $(`#${sliderId}`).owlCarousel({
            items: 1,
            loop: true,
            nav: false,
            dots: false,
            margin: 10
        });
    });

    const prevButtons = document.querySelectorAll('.carousel-prev');
    const nextButtons = document.querySelectorAll('.carousel-next');
    prevButtons.forEach(button => {
        button.addEventListener('click', () => {
            const sliderId = button.getAttribute('data-slider');
            $(`#${sliderId}`).trigger('prev.owl.carousel');
        });
    });
    nextButtons.forEach(button => {
        button.addEventListener('click', () => {
            const sliderId = button.getAttribute('data-slider');
            $(`#${sliderId}`).trigger('next.owl.carousel');
        });
    });
}

window.onload = function () {
    initSliders();
};

$(document).ready(function () {
    $('#search').click(function () {
        $.ajax({
            type: 'GET',
            url: '/ilan/filter/',
            data: {
                'category': $('select[name=category]').val(),
                'room': $('select[name=room]').val(),
                'geo': $('select[name=geo]').val(),
                'min': $('input[name=min]').val(),
                'max': $('input[name=max]').val(),
                'id': $('input[name=id]').val()
            },
            success: function (data) {
                // Обработка успешного ответа от сервера
                console.log(data)
                $('.product-grid').empty();
                for (var i = 0; i < data.length; i++) {
                    var product = data[i];
                    var html = '<div class="product-card">';
                    html += '<div class="slider owl-carousel" id="slider' + product.id + '">';
                    for (var j = 0; j < product.images.length; j++) {
                        html += '<div><img src="' + product.images[j].url + '" onerror="' + product.images[j].url + '" alt="Product 1" class="image" width="350" height="290"></div>';
                    }
                    html += '</div>';
                    html += '<div class="carousel-nav">';
                    html += '<button class="carousel-prev" data-slider="slider' + product.id + '"><i class="fa fa-angle-left"></i></button>';
                    html += '<button class="carousel-next" data-slider="slider' + product.id + '"><i class="fa fa-angle-right"></i></button>';
                    html += '</div>';
                    html += '<ul class="action_product">';
                    html += '<li class="id_product"><span>ID&nbsp</span><br><span>' + product.id + '</span></li>';
                    html += '<li><img src="/static/img/favorit.svg" onclick="addFavorite(' + product.id + ')" alt="love"></li>';
                    html += '<li><img src="/static/img/like.svg" onclick="addLike(' + product.id + ')" alt="like"></li>';
                    html += '<li><img src="/static/img/dislike.svg" onclick="addDislike(' + product.id + ')" alt="dislike"></li>';
                    html += '</ul>';
                    html += '<div class="description_product">';
                    html += '<div class="description_list">';
                    html += '<div class="item-list">';
                    html += '<div class="title-list">' + product.title + '</div>';
                    html += '</div>';
                    html += '<div class="item-list">';
                    html += '<div class="price-item">';
                    html += '<ul>';
                    html += '<li>Цена</li>';
                    html += '<li>от ' + product.price + ' USD</li>';
                    html += '</ul>';
                    html += '</div>';
                    html += '</div>';
                    html += '<div class="item-list">';
                    html += '<div class="square-item">';
                    html += '<ul>';
                    html += '<li>Площадь</li>';
                    html += '<li>' + product.area + ' кв.м</li>';
                    html += '</ul>';
                    html += '</div>';
                    html += '</div>';
                    html += '<div class="item-list">';
                    html += '<div class="rooms-list">';
                    html += '<ul>';
                    html += '<li>Комнаты</li>';
                    html += '<li><ul>';
                    for (var k = 0; k < product.rooms.length; k++) {
                        if (k !== 0) {
                            html += ', ';
                        }
                        html += '<li>' + product.rooms[k].title + '</li>';
                    }

                    html += '</ul></li>';
                    html += '</ul>';
                    html += '</div>';
                    html += '</div>';
                    html += '</div>';
                    html += '</div>'; // закрываем блок с информацией о продукте
                    html += '<a href="#" class="btn-more">Подробнее</a>';
                    html += '</div>'; // закрываем блок с классом "product-card"
                    $('.product-grid').append(html);
                    initSliders();

                }
            },
            error: function (xhr, textStatus, errorThrown) {
                // Обработка ошибок запроса
                console.log(xhr.responseText);
            }
        });
    })
    ;
});