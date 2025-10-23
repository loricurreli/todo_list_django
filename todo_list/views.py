from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from todo_list.models import Todo
from todo_list.forms import FormTask, UserForm, UserProfileInfoForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    context = {'todos_list': Todo.objects.all().order_by('id') }
    return render(request, 'todo_list/index.html', context)


def users(request):
    users_list = {'users_list': User.objects.all().order_by('id')}
    return render(request, 'todo_list/users.html', context=users_list)

@login_required
def new_task(request):
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Task creato con successo.")
                return redirect("todo_list:index")
            except Exception as exc:
                messages.error(request, f"Errore durante il salvataggio: {exc}")
        else:
            messages.error(request, "Controlla i campi del form.")
    else:
        form = FormTask()

    return render(request, "todo_list/new_task.html", {"form": form})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                registered = True
                messages.success(request, "Registrazione completata con successo. Puoi ora accedere.")
            except Exception as exc:
                messages.error(request, f"Errore durante la registrazione: {exc}")
        else:
            messages.error(request, "Controlla i campi evidenziati e riprova.")
    else:
        user_form = UserForm()
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
