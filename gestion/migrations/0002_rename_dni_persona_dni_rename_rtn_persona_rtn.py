# Generated by Django 5.1.4 on 2024-12-13 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='DNI',
            new_name='dni',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='RTN',
            new_name='rtn',
        ),
    ]