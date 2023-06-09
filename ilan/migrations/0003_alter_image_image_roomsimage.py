# Generated by Django 4.1.7 on 2023-04-16 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0002_remove_product_area_ar_remove_product_area_de_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='Разрешение изображения должно быть 1920x1080 и выше', upload_to='', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='RoomsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Разрешение изображения должно быть 1920x1080 и выше', upload_to='', verbose_name='Изображение комнат')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images_rooms', to='ilan.product')),
            ],
            options={
                'verbose_name': 'Изображение комнаты',
                'verbose_name_plural': 'Изображения комнат',
            },
        ),
    ]
