# Generated by Django 2.2.6 on 2020-09-18 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('words_count', models.IntegerField()),
                ('http_status_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_status', models.SmallIntegerField(choices=[(3, 'FINISHED'), (1, 'NOT_STARTED'), (2, 'PENDING')], default=1, max_length=1)),
                ('http_status', models.IntegerField()),
            ],
        ),
    ]