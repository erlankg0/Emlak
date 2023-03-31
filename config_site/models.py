from django.core.exceptions import ValidationError
from django.db import models


class Logo(models.Model):
    logo = models.ImageField(
        verbose_name='Логотип',
        help_text='Логотип компании',
        upload_to='logo'
    )  # логотип компании

    def __str__(self):
        return f'Логотип {self.pk}'

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'


class Title(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Заголовок страницы",
        unique=True
    )  # заголовок страницы

    # singelton pattern
    def save(self, *args, **kwargs):
        if Title.objects.exists() and not self.pk:
            raise ValidationError('Заголовок уже существует, Удалите старый создайте новый')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'
        db_table = 'title'


class SubTitle(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Заголовок страницы",
        unique=True
    )  # заголовок страницы

    # singelton pattern
    def save(self, *args, **kwargs):
        if Title.objects.exists() and not self.pk:
            raise ValidationError('Заголовок уже существует, Удалите старый создайте новый')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'
        db_table = 'title'


class Favicon(models.Model):
    favicon = models.ImageField(
        upload_to='favicon/',
        verbose_name='Иконка',
        help_text='Иконка',
    )  # иконка

    def get_last_favicon(self):
        return Favicon.objects.last()

    class Meta:
        verbose_name = 'Иконка'
        verbose_name_plural = 'Иконки'
        db_table = 'favicon'
