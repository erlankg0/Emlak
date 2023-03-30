from django.db import models


class Category(models.Model):
    title = models.CharField(
        verbose_name="Название типа (Квартира)",
        max_length=80,
        unique=True,
        help_text="Максимум 80 символов."
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
        db_table = "categories"


class Rooms(models.Model):
    title = models.CharField(
        verbose_name="Комнаты в квартире (1+1)",
        max_length=50,
        unique=True,
        help_text="Максимум 50 символов"

    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"
        db_table = "rooms"


class Area(models.Model):
    title = models.CharField(
        verbose_name="Район (Alanya)",
        max_length=100,
        unique=True,
        help_text="Максимум 100 символов"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        db_table = "areas"


# Модель Ip адреса
class Ip(models.Model):
    ip = models.GenericIPAddressField(
        verbose_name='IP address',
        help_text='IP address',
        unique=True,
    )  # IP адрес

    def __str__(self):  # Возвращает IP адрес
        return self.ip

    class Meta:
        verbose_name = 'IP адрес'  # Имя модели
        verbose_name_plural = 'IP адреса'  # Имя модели во множественном числе
        db_table = 'ip'  # Имя таблицы

