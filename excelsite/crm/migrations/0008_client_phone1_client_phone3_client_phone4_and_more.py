# Generated by Django 4.2 on 2023-12-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_rename_min_square_zayavki_square_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Доп1. телефон клиента'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Доп3. телефон клиента'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Доп4. телефон клиента'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone5',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Доп5. телефон клиента'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Доп2. телефон клиента'),
        ),
    ]
