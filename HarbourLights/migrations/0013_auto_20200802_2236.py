# Generated by Django 3.0.8 on 2020-08-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarbourLights', '0012_auto_20200802_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.CharField(max_length=20),
        ),
    ]