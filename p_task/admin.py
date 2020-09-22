from django.contrib import admin
#импортируем модели
from p_task.models import Tasks,Results

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Results)
class ResultAdmin(admin.ModelAdmin):
    pass

# Register your models here.
