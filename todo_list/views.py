from django.shortcuts import render
from django.http import HttpResponse
from todo_list.models import Todo, User

# Create your views here.
def index(request):
    todos_list = {'todos_list': Todo.objects.all().order_by('id')}
    return render(request, 'todo_list/index.html', context=todos_list)


def users(request):
    users_list = {'users_list': User.objects.all().order_by('id')}
    return render(request, 'todo_list/users.html', context=users_list)