# Generated by Django 4.2 on 2023-12-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0002_alter_realty_options_remove_pages_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realty',
            name='price_rent',
        ),
        migrations.RemoveField(
            model_name='realty',
            name='price_sale',
        ),
        migrations.AddField(
            model_name='realty',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.RemoveField(
            model_name='realty',
            name='categ',
        ),
        migrations.AddField(
            model_name='realty',
            name='categ',
            field=models.ManyToManyField(related_name='Категория', to='korp.category', verbose_name='Категория'),
        ),
    ]
