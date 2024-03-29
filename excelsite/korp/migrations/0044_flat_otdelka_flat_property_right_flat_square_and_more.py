# Generated by Django 4.2 on 2024-02-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0043_alter_land_commission'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('Без отделки', 'Без отделки'), ('Предчистовая', 'Предчистовая'), ('Чистовая', 'Чистовая')], help_text=' обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AddField(
            model_name='flat',
            name='property_right',
            field=models.CharField(choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик')], max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AddField(
            model_name='flat',
            name='square',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Площадь кв.м.'),
        ),
        migrations.AlterField(
            model_name='tc',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('Без отделки', 'Без отделки'), ('Чистовая', 'Чистовая'), ('Офисная', 'Офисная')], help_text=' обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание', max_length=50, null=True, verbose_name='Отделка'),
        ),
    ]
