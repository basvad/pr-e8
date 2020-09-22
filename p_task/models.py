from django.db import models
from django.utils import timezone  
from django.utils.timezone import localtime, now
import datetime

#модель храненение результатов
class Results(models.Model):
    address = models.CharField(max_length=300)
    words_count = models.IntegerField()
    http_status_code = models.IntegerField()

#хранение задач
class Tasks(models.Model):
    NOT_STARTED = 1
    PENDING = 2
    FINISHED = 3
    STATUS_CHOICES = {
        (NOT_STARTED,'NOT_STARTED'),
        (PENDING,'PENDING'),
        (FINISHED, 'FINISHED')
    }
    address = models.URLField()
    timestamp = models.DateTimeField(default=datetime.datetime.now())  
    task_status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NOT_STARTED)
    http_status = models.IntegerField(null=True)