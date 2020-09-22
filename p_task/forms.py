from django import forms  
from p_task.models import Tasks
from .parsite import parsite

  
class TasksForm(forms.ModelForm): 
    address = forms.URLField(label="",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Адрес сайта"}))   
    class Meta:  
        model = Tasks  
        fields = ('address',)
    #def parse_site(self):
        #доступ к полям формы
        #print(self.cleaned_data['address'])
    #    return parsite(self.cleaned_data['address'])