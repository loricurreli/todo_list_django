from django import forms
from todo_list.models import Todo
from django.contrib.auth.models import User
from todo_list.models import UserProfileInfo

class FormTask(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

class UserFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


    
    
