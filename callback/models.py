from django.db import models
from ilan.models import Product


class Callback(models.Model):
    customer_email = models.EmailField(
        verbose_name='Э-Почта Клиента',
        max_length=300,
    )
    customer_phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=20,
    )
    customer_name = models.CharField(
        verbose_name='Имя Клиента',
        max_length=250,
    )
    id_product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name='ID объекта'
    )
    message = models.TextField(
        verbose_name='Сообщение Клиента',
        max_length=2000,
    )
    checked = models.BooleanField(
        verbose_name='Проверено или НЕТ',
        default=True,
    )

    def __str__(self):
        return f'Имя: {self.customer_name}, email: {self.customer_email}, Тел.{self.customer_phone}'

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'
        db_table = 'callback'
        ordering = ['checked']