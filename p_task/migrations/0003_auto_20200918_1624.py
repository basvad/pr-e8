# Generated by Django 2.2.6 on 2020-09-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_task', '0002_auto_20200918_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='address',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_status',
            field=models.SmallIntegerField(choices=[(1, 'NOT_STARTED'), (3, 'FINISHED'), (2, 'PENDING')], default=1),
        ),
    ]
