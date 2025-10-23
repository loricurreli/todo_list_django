from django import forms
from todo_list.models import Todo
from django.contrib.auth.models import User
from todo_list.models import UserProfileInfo

class FormTask(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


    
    
