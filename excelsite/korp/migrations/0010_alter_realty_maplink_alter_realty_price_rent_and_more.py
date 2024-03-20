# Generated by Django 4.2 on 2023-12-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0009_alter_realty_buildclass_alter_realty_buildtype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='maplink',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на яндекс карту'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='price_rent',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='Цена аренды'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='price_sale',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='Цена продажи'),
        ),
    ]
