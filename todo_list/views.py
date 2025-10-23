from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from todo_list.models import Todo, AppUser
from todo_list.forms import FormTask, UserFrom, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):    
    context_dict = {'text': 'hello world', 'number': 100, 'todos_list': Todo.objects.all().order_by('id') }
    return render(request, 'todo_list/index.html', context_dict)


def users(request):
    users_list = {'users_list': AppUser.objects.all().order_by('id')}
    return render(request, 'todo_list/users.html', context=users_list, )

def new_task(request):
    form = FormTask()
    
    if request.method == 'POST':
        form = FormTask(request.POST)
        if form.is_valid():
           form.save(commit=True)
           return index(request)
        else:
            print('ERROR FORM INVALID')
       
    return render(request, 'todo_list/new_task.html', { 'form': form})

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserFrom(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
           user = user_form.save()
           user.set_password(user.password)
           user.save()
           
           profile = profile_form.save(commit=False)
           profile.user = user
           
           if 'profile_pic' in request.FILES:
               profile.profile_pic = request.FILES['profile_pic']
            
           profile.save()
           
           registered=True
        else:
            print('ERROR FORM INVALID')
    else:
        user_form = UserFrom()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'todo_list/register.html', {'user_form': user_form, 'registered': registered, 'profile_form': profile_form})
        
       
def user_login(request):
    
    if request.method == 'POST':
        username = request.post.get("username")
        password = request.post.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username=username, password=password))
    
    else: 
        return render(request, 'todo_list/login.html')
    
def user_logout(request):
    # logout(request)
    return render(request, 'todo_list/logout.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")
