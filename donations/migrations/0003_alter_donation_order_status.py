# Generated by Django 4.0.1 on 2022-01-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_donation_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='order_status',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
