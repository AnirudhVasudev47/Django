# Generated by Django 3.0.8 on 2020-08-01 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HarbourLights', '0008_booking_totalamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='TotalAmount',
        ),
    ]