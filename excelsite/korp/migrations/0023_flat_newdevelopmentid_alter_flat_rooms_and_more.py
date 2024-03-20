# Generated by Django 4.2 on 2024-01-08 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0022_remove_flat_bc_remove_flat_buildclass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='NewDevelopmentId',
            field=models.CharField(max_length=300, null=True, verbose_name='ID объекта из XML-справочника. Если в жилом комплексе новостроек есть корпуса, то обязательно ID корпуса (элементы Housing); если корпусов нет, то ID жилого комплекса (элементы Object)'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='rooms',
            field=models.CharField(choices=[('Студия', 'Студия'), ('Своб. планировка', 'Своб. планировка'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10 и более', '10 и более')], max_length=100, null=True, verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='status',
            field=models.CharField(choices=[('Квартира', 'Квартира'), ('Апартаменты', 'Апартаменты')], max_length=100, null=True, verbose_name='Статус'),
        ),
    ]