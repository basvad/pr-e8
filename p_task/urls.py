from django.urls import path  
from p_task.views import TaskCreate,ResultList
app_name = 'p_task' 
urlpatterns = [
    path('', TaskCreate.as_view(), name='task_create'),
    path("results/", ResultList.as_view(), name='task_list'),
]
  