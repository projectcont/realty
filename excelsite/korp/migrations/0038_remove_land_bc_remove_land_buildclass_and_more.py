# Generated by Django 4.2 on 2024-02-06 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0037_remove_flat_square_remove_tc_entrance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='bc',
        ),
        migrations.RemoveField(
            model_name='land',
            name='buildclass',
        ),
        migrations.RemoveField(
            model_name='land',
            name='buildtype',
        ),
        migrations.RemoveField(
            model_name='land',
            name='entrance',
        ),
        migrations.RemoveField(
            model_name='land',
            name='height',
        ),
        migrations.RemoveField(
            model_name='land',
            name='layout',
        ),
        migrations.RemoveField(
            model_name='land',
            name='otdelka',
        ),
        migrations.RemoveField(
            model_name='land',
            name='parking',
        ),
        migrations.RemoveField(
            model_name='land',
            name='square',
        ),
    ]