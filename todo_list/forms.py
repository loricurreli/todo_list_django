from django import forms
from todo_list.models import Todo


class FormTask(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
    