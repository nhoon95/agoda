# Generated by Django 2.2.5 on 2020-12-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20201107_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('peding', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='peding', max_length=20),
        ),
    ]
