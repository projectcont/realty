# Generated by Django 4.2 on 2024-01-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_zayavki_scan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scanresult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realty_number', models.CharField(max_length=255, verbose_name='Количество объектов просканировано')),
                ('zav_number', models.CharField(max_length=255, verbose_name='Количество заявок просканировано')),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Сканирование',
                'verbose_name_plural': 'Сканирования',
                'ordering': ['time_update'],
            },
        ),
    ]
