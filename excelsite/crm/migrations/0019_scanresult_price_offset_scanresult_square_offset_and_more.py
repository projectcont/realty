# Generated by Django 4.2 on 2024-01-21 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_scanresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='price_offset',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=10, verbose_name='Допуск цены'),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='square_offset',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=10, verbose_name='Допуск площади'),
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='realty_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество объектов просканировано'),
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='zav_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество заявок просканировано'),
        ),
    ]
