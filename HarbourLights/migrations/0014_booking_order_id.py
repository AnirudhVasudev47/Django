# Generated by Django 3.0.8 on 2020-08-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarbourLights', '0013_auto_20200802_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='order_id',
            field=models.CharField(default='text', max_length=30),
            preserve_default=False,
        ),
    ]
