from django import forms 
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(label='title', max_length=100 ,
    widget=forms.TextInput(attrs={'class': "form-control mx-2"}))
    # completed = forms.BooleanField(label='Completed', class='form-check-input')
    class Meta:
        model = Task
        fields = "__all__"