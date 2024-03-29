# Generated by Django 4.2 on 2024-01-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0025_alter_flat_options_remove_flat_newdevelopmentid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bc',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='bc',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='flat',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='land',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='land',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='ofis',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='ofis',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='proizv',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='proizv',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='psn',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='psn',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='retail',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='retail',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='tc',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='tc',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.AlterField(
            model_name='torg',
            name='otdelka',
            field=models.CharField(blank=True, choices=[('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная')], help_text=' (обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание)', max_length=50, null=True, verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='torg',
            name='sale_right',
            field=models.CharField(blank=True, choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
    ]
