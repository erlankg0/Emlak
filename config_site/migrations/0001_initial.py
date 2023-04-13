# Generated by Django 4.1.7 on 2023-03-31 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(help_text='Иконка', upload_to='favicon/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Иконка',
                'verbose_name_plural': 'Иконки',
                'db_table': 'favicon',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(help_text='Логотип компании', upload_to='logo', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Логотип',
                'verbose_name_plural': 'Логотипы',
            },
        ),
        migrations.CreateModel(
            name='SubTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Заголовок страницы', max_length=255, unique=True, verbose_name='Заголовок')),
                ('name_ru', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_en', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_tr', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_ar', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_de', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовки',
                'db_table': 'subtitle',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Заголовок страницы', max_length=255, unique=True, verbose_name='Заголовок')),
                ('name_ru', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_en', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_tr', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_ar', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
                ('name_de', models.CharField(help_text='Заголовок страницы', max_length=255, null=True, unique=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовки',
                'db_table': 'title',
            },
        ),
    ]