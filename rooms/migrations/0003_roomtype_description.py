# Generated by Django 2.2.5 on 2020-11-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20201103_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
