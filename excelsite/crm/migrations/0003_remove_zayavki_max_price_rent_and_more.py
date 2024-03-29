# Generated by Django 4.2 on 2023-12-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_zayavki_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zayavki',
            name='max_price_rent',
        ),
        migrations.RemoveField(
            model_name='zayavki',
            name='max_price_sale',
        ),
        migrations.AddField(
            model_name='zayavki',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='макс. цена'),
        ),
        migrations.AddField(
            model_name='zayavki',
            name='rent_sale',
            field=models.CharField(blank=True, choices=[('rent', 'аренда'), ('sale', 'продажа')], help_text='Аренда/продажа', max_length=5, verbose_name='Аренда/продажа'),
        ),
    ]
