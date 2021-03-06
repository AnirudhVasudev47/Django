# Generated by Django 3.0.8 on 2020-08-01 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HarbourLights', '0005_auto_20200801_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('no_of_guest', models.IntegerField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HarbourLights.Rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
