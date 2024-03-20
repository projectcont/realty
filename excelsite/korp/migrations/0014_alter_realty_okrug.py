# Generated by Django 4.2 on 2023-12-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0013_alter_realty_okrug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='okrug',
            field=models.CharField(choices=[('1', 'Центральный'), ('Северный', 'Северный'), ('Северо-Восточный', 'Северо-Восточный'), ('Восточный', 'Восточный'), ('Юго-Восточный', 'Юго-Восточный'), ('Южный', 'Южный'), ('Юго-Западный', 'Юго-Западный'), ('Западный', 'Западный'), ('Северо-Западный', 'Северо-Западный'), ('Зеленоградский', 'Зеленоградский'), ('Троицкий', 'Троицкий'), ('Новомосковский', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
    ]
