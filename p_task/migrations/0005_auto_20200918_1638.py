# Generated by Django 2.2.6 on 2020-09-18 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_task', '0004_auto_20200918_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 16, 38, 0, 202378)),
        ),
    ]
