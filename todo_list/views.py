from django.shortcuts import render
from django.http import HttpResponse
from todo_list.models import Todo, User
from todo_list.forms import FormTask

# Create your views here.
def index(request):
    todos_list = {'todos_list': Todo.objects.all().order_by('id')}
    return render(request, 'todo_list/index.html', context=todos_list)


def users(request):
    users_list = {'users_list': User.objects.all().order_by('id')}
    return render(request, 'todo_list/users.html', context=users_list)

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