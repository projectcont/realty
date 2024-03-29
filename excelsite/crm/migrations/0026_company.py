# Generated by Django 4.2 on 2024-03-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_alter_export_options_remove_export_is_using_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='partners/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Портнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
    ]
