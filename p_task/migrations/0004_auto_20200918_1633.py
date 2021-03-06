# Generated by Django 2.2.6 on 2020-09-18 13:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('p_task', '0003_auto_20200918_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_status',
            field=models.SmallIntegerField(choices=[(1, 'NOT_STARTED'), (2, 'PENDING'), (3, 'FINISHED')], default=1),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 13, 33, 37, 53593, tzinfo=utc)),
        ),
    ]
