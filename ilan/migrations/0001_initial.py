# Generated by Django 4.1.7 on 2023-03-31 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Максимум 250 символов', max_length=250, unique=True, verbose_name='Название (Квартиры с концепцией отеля)')),
                ('title_ru', models.CharField(help_text='Максимум 250 символов', max_length=250, null=True, unique=True, verbose_name='Название (Квартиры с концепцией отеля)')),
                ('title_en', models.CharField(help_text='Максимум 250 символов', max_length=250, null=True, unique=True, verbose_name='Название (Квартиры с концепцией отеля)')),
                ('title_tr', models.CharField(help_text='Максимум 250 символов', max_length=250, null=True, unique=True, verbose_name='Название (Квартиры с концепцией отеля)')),
                ('title_ar', models.CharField(help_text='Максимум 250 символов', max_length=250, null=True, unique=True, verbose_name='Название (Квартиры с концепцией отеля)')),
                ('title_de', models.CharField(help_text='Максимум 250 символов', max_length=250, null=True, unique=True, verbose_name='Название (Квартиры с концепцией отеля)')),
                ('description', models.TextField(verbose_name='Описание объявления')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание объявления')),
                ('description_en', models.TextField(null=True, verbose_name='Описание объявления')),
                ('description_tr', models.TextField(null=True, verbose_name='Описание объявления')),
                ('description_ar', models.TextField(null=True, verbose_name='Описание объявления')),
                ('description_de', models.TextField(null=True, verbose_name='Описание объявления')),
                ('price', models.CharField(help_text='Максимум 20 символов', max_length=20, verbose_name='Цена')),
                ('square', models.PositiveSmallIntegerField(verbose_name='Площадь')),
                ('square_ru', models.PositiveSmallIntegerField(null=True, verbose_name='Площадь')),
                ('square_en', models.PositiveSmallIntegerField(null=True, verbose_name='Площадь')),
                ('square_tr', models.PositiveSmallIntegerField(null=True, verbose_name='Площадь')),
                ('square_ar', models.PositiveSmallIntegerField(null=True, verbose_name='Площадь')),
                ('square_de', models.PositiveSmallIntegerField(null=True, verbose_name='Площадь')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Активный или Скрытый', verbose_name='Активный')),
                ('slug', models.SlugField(help_text='Max 100 symbols, unique e.g. "alanya-villa-270"', max_length=100, unique=True, verbose_name='URL')),
                ('top_offer', models.BooleanField(default=False, help_text='Да/Нет (по умолчанию НЕТ)', verbose_name='Топ предложений')),
                ('new_offer', models.BooleanField(default=False, help_text='Да/Нет (по умолчанию НЕТ)', verbose_name='Новые предложения')),
                ('hot_deal', models.BooleanField(default=False, help_text='Да/Нет (по умолчанию НЕТ)', verbose_name='Горячие предложения')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.area', verbose_name='Район (Местонахождения)')),
                ('area_ar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.area', verbose_name='Район (Местонахождения)')),
                ('area_de', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.area', verbose_name='Район (Местонахождения)')),
                ('area_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.area', verbose_name='Район (Местонахождения)')),
                ('area_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.area', verbose_name='Район (Местонахождения)')),
                ('area_tr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.area', verbose_name='Район (Местонахождения)')),
                ('category', models.ForeignKey(help_text='Например (Дом).', on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
                ('category_ar', models.ForeignKey(help_text='Например (Дом).', null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
                ('category_de', models.ForeignKey(help_text='Например (Дом).', null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
                ('category_en', models.ForeignKey(help_text='Например (Дом).', null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
                ('category_ru', models.ForeignKey(help_text='Например (Дом).', null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
                ('category_tr', models.ForeignKey(help_text='Например (Дом).', null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
                ('rooms', models.ManyToManyField(to='home.rooms', verbose_name='Комнаты')),
                ('rooms_ar', models.ManyToManyField(null=True, to='home.rooms', verbose_name='Комнаты')),
                ('rooms_de', models.ManyToManyField(null=True, to='home.rooms', verbose_name='Комнаты')),
                ('rooms_en', models.ManyToManyField(null=True, to='home.rooms', verbose_name='Комнаты')),
                ('rooms_ru', models.ManyToManyField(null=True, to='home.rooms', verbose_name='Комнаты')),
                ('rooms_tr', models.ManyToManyField(null=True, to='home.rooms', verbose_name='Комнаты')),
                ('view', models.ManyToManyField(blank=True, help_text='view count', null=True, related_name='view_products', to='home.ip', verbose_name='View')),
            ],
            options={
                'verbose_name': 'Объявления',
                'verbose_name_plural': 'Объявлении',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.ForeignKey(help_text='IP address', on_delete=django.db.models.deletion.CASCADE, to='home.ip', verbose_name='IP address')),
                ('product', models.ForeignKey(help_text='Product', on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='ilan.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Нравится',
                'verbose_name_plural': 'Нравится',
                'db_table': 'like',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Разрешение изображения должно быть 1920x1080', upload_to='', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='ilan.product')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.ForeignKey(help_text='IP', on_delete=django.db.models.deletion.CASCADE, to='home.ip', verbose_name='IP пользователя')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='ilan.product', verbose_name='Не нравится')),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.ForeignKey(help_text='IP', on_delete=django.db.models.deletion.CASCADE, to='home.ip', verbose_name='IP пользователя')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='ilan.product', verbose_name='Не нравится')),
            ],
        ),
    ]