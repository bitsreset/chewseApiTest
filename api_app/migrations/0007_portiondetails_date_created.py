# Generated by Django 2.2.6 on 2019-10-30 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0006_auto_20191030_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='portiondetails',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
