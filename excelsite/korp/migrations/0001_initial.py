# Generated by Django 4.2 on 2023-12-14 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название категории', max_length=100, verbose_name='Название категории')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('metatitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='meta title')),
                ('metadescription', models.TextField(blank=True, null=True, verbose_name='meta description')),
                ('alias', models.CharField(blank=True, max_length=255, null=True, verbose_name='alias')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('rent', 'АРЕНДА'), ('sale', 'ПРОДАЖА')], help_text='Аренда/продажа', max_length=100, verbose_name='Аренда/продажа')),
            ],
            options={
                'verbose_name': 'Аренда/продажа',
                'verbose_name_plural': 'Аренда/продажа',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('adres', models.TextField(verbose_name='Адрес')),
                ('map', models.TextField(verbose_name='Код с яндекс карты')),
                ('square', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Площадь кв.м.')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('rent_sale', models.CharField(choices=[('rent', 'аренда'), ('sale', 'продажа')], help_text='Аренда/продажа', max_length=5, verbose_name='Аренда/продажа')),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена продажи, руб')),
                ('price_rent', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена аренды, руб/мес')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('photo6', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('maplink', models.TextField(blank=True, null=True, verbose_name='Ссылка на яндекс карту')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('floors', models.IntegerField(blank=True, null=True, verbose_name='Этажность')),
                ('export_avito', models.BooleanField(default=False)),
                ('export_yandex', models.BooleanField(default=False)),
                ('export_3', models.BooleanField(default=False)),
                ('export_4', models.BooleanField(default=False)),
                ('export_5', models.BooleanField(default=False)),
                ('export_6', models.BooleanField(default=False)),
                ('ownerphone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон владельца')),
                ('owneremail', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email владельца')),
                ('buildclass', models.CharField(blank=True, choices=[('a', 'А'), ('aplus', 'А+'), ('b', 'B'), ('bplus', 'B+'), ('c', 'C'), ('cplus', 'C+'), ('d', 'D'), ('dplus', 'D+')], help_text='Класс здания', max_length=10, null=True, verbose_name='Класс здания')),
                ('bc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование БЦ')),
                ('buildtype', models.CharField(blank=True, choices=[('1', 'Жилое'), ('2', 'Бизнес квартал')], help_text='Тип здания', max_length=100, null=True, verbose_name='Тип здания')),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='korp.category', verbose_name='Категория')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['time_create', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='контент')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Модифицировано')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='korp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
