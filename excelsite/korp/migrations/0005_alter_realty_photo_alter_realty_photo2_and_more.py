# Generated by Django 4.2 on 2023-12-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0004_pages_metadescription_pages_metatitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/osn', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='Фото'),
        ),
    ]