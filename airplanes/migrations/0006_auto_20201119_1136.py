# Generated by Django 2.2.5 on 2020-11-19 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airplanes', '0005_auto_20201117_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airplane',
            old_name='user',
            new_name='users',
        ),
    ]
