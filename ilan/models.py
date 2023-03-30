from django.db import models
from home.models import Category, Area, Rooms, Ip


class Product(models.Model):
    title = models.CharField(
        verbose_name="Название (Квартиры с концепцией отеля)",
        max_length=250,
        help_text="Максимум 250 символов",
        unique=True
    )
    description = models.TextField(
        verbose_name="Описание объявления"
    )
    price = models.CharField(
        verbose_name="Цена",
        max_length=20,
        help_text='Максимум 20 символов'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        help_text="Например (Дом).",
    )
    square = models.PositiveSmallIntegerField(
        verbose_name="Площадь",
    )
    rooms = models.ManyToManyField(
        Rooms,
        verbose_name="Комнаты",
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.PROTECT,
        verbose_name="Район (Местонахождения)"
    )
    view = models.ManyToManyField(
        Ip,  # Ip адрес
        verbose_name='View',  # Просмотр
        related_name='view_products',  # related_name='view_products'
        help_text='view count',  # Просмотры
        blank=True,
        null=True,
    )  # View
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )  # Дата создания
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )  # Дата обновления
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный',
        help_text='Активный или Скрытый',
    )  # Активный
    slug = models.SlugField(
        max_length=100,  # Максимальная длина 100 символов
        verbose_name='URL',  # URL
        help_text='Max 100 symbols, unique e.g. "alanya-villa-270"',  # URL
        unique=True,
    )  # URL продукта
    top_offer = models.BooleanField(
        help_text="Да/Нет (по умолчанию НЕТ)",
        verbose_name="Топ предложений",
        default=False,
    )
    new_offer = models.BooleanField(
        help_text="Да/Нет (по умолчанию НЕТ)",
        verbose_name="Новые предложения",
        default=False,
    )
    hot_deal = models.BooleanField(
        help_text="Да/Нет (по умолчанию НЕТ)",
        verbose_name="Горячие предложения",
        default=False,
    )

    def __str__(self):
        return self.title

    def has_liked(self, ip):
        return self.likes.filter(ip=ip).exists()

    def has_disliked(self, ip):
        return self.dislikes.filter(ip=ip).exists()

    def has_favorited(self, ip):
        return self.favorites.filter(ip=ip).exists()

    def get_view_count(self):  # Возвращает количество просмотров
        return self.view.count()

    def get_popular_products(self):  # Возвращает популярные продукты
        return self.objects.filter(is_active=True).order_by('-view')

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявлении'

class Image(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        help_text='Разрешение изображения должно быть 1920x1080',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='images'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


# Модель Like
class Like(models.Model):
    ip = models.ForeignKey(
        Ip,
        on_delete=models.CASCADE,
        verbose_name='IP address',
        help_text='IP address',

    )  # IP адрес
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name='Product',
        help_text='Product',
        related_name="likes",
    )  # Продукт

    def __str__(self):  # Возвращает IP адрес и продукт
        return f'{self.ip} - {self.product}'

    class Meta:
        verbose_name = 'Нравится'  # Имя модели
        verbose_name_plural = 'Нравится'  # Имя модели во множественном числе
        db_table = 'like'  # Имя таблицы


class Dislike(models.Model):
    ip = models.ForeignKey(
        Ip,
        on_delete=models.CASCADE,
        verbose_name="IP пользователя",
        help_text="IP"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Не нравится",
        related_name="dislikes",
    )


class Favorite(models.Model):
    ip = models.ForeignKey(
        Ip,
        on_delete=models.CASCADE,
        verbose_name="IP пользователя",
        help_text="IP"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Не нравится",
        related_name="favorites",
    )
