# Generated by Django 4.1.7 on 2023-03-31 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Максимум 100 символов', max_length=100, unique=True, verbose_name='Район (Alanya)')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Максимум 80 символов.', max_length=80, unique=True, verbose_name='Название типа (Квартира)')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(help_text='IP address', unique=True, verbose_name='IP address')),
            ],
            options={
                'verbose_name': 'IP адрес',
                'verbose_name_plural': 'IP адреса',
                'db_table': 'ip',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Максимум 50 символов', max_length=50, unique=True, verbose_name='Комнаты в квартире (1+1)')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
                'db_table': 'rooms',
            },
        ),
    ]
