# Generated by Django 4.2 on 2023-12-16 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_zayavki_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zayavki',
            name='rent_sale',
        ),
    ]
