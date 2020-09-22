from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from p_task.models import Tasks,Results
from django.shortcuts import redirect
from p_task.forms import TasksForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .parsite import parsite


class TaskCreate(CreateView):  
    model = Tasks
    #ссылка на класс формы  
    form_class = TasksForm 
    #адрес страницы, на которую последует редирект 
    success_url = reverse_lazy('p_task:task_create')
    #название необходимого шаблона  
    template_name = 'task_form.html'
    #вызывается автоматически в случае корректности данных, переданных пользователем
    def form_valid(self, form):
        # Мы используем ModelForm, а его метод save() возвращает инстанс
        # модели, связанный с формой. Аргумент commit=False говорит о том, что
        # записывать модель в базу рановато.
        #instance = form.save(commit=False)
        instance = form.save()
        parsite(instance)
        #print ('ID: {}'.format(result))
        #print ('ID: {}'.format(instance.id))
        # Теперь, когда у нас есть несохранённая модель, можно ей чего-нибудь
        # накрутить.
        #instance.http_status = form.parse_site()
        # form.parse_site()
        # А теперь можно сохранить в базу
        #instance.save() 
        #То есть нам нужно создать объект модели задачи с соответствующими параметрами, а потом запустить задачу.
        return super().form_valid(form)  

class ResultList (ListView):
    #модель
    model = Results
    # шаблон
    template_name = "results.html"
    # имя переменной, в которой хранится список объектов для отображения
    context_object_name = "result_list"
    #постраничный вывод
    paginate_by = 50