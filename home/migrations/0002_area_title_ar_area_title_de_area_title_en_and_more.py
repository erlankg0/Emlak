# Generated by Django 4.1.7 on 2023-04-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='title_ar',
            field=models.CharField(help_text='Максимум 100 символов', max_length=100, null=True, unique=True, verbose_name='Район (Alanya)'),
        ),
        migrations.AddField(
            model_name='area',
            name='title_de',
            field=models.CharField(help_text='Максимум 100 символов', max_length=100, null=True, unique=True, verbose_name='Район (Alanya)'),
        ),
        migrations.AddField(
            model_name='area',
            name='title_en',
            field=models.CharField(help_text='Максимум 100 символов', max_length=100, null=True, unique=True, verbose_name='Район (Alanya)'),
        ),
        migrations.AddField(
            model_name='area',
            name='title_ru',
            field=models.CharField(help_text='Максимум 100 символов', max_length=100, null=True, unique=True, verbose_name='Район (Alanya)'),
        ),
        migrations.AddField(
            model_name='area',
            name='title_tr',
            field=models.CharField(help_text='Максимум 100 символов', max_length=100, null=True, unique=True, verbose_name='Район (Alanya)'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ar',
            field=models.CharField(help_text='Максимум 80 символов.', max_length=80, null=True, unique=True, verbose_name='Название типа (Квартира)'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_de',
            field=models.CharField(help_text='Максимум 80 символов.', max_length=80, null=True, unique=True, verbose_name='Название типа (Квартира)'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(help_text='Максимум 80 символов.', max_length=80, null=True, unique=True, verbose_name='Название типа (Квартира)'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(help_text='Максимум 80 символов.', max_length=80, null=True, unique=True, verbose_name='Название типа (Квартира)'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_tr',
            field=models.CharField(help_text='Максимум 80 символов.', max_length=80, null=True, unique=True, verbose_name='Название типа (Квартира)'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='title_ar',
            field=models.CharField(help_text='Максимум 50 символов', max_length=50, null=True, unique=True, verbose_name='Комнаты в квартире (1+1)'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='title_de',
            field=models.CharField(help_text='Максимум 50 символов', max_length=50, null=True, unique=True, verbose_name='Комнаты в квартире (1+1)'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='title_en',
            field=models.CharField(help_text='Максимум 50 символов', max_length=50, null=True, unique=True, verbose_name='Комнаты в квартире (1+1)'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='title_ru',
            field=models.CharField(help_text='Максимум 50 символов', max_length=50, null=True, unique=True, verbose_name='Комнаты в квартире (1+1)'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='title_tr',
            field=models.CharField(help_text='Максимум 50 символов', max_length=50, null=True, unique=True, verbose_name='Комнаты в квартире (1+1)'),
        ),
    ]
