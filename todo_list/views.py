from django.shortcuts import redirect, render
from django.http import HttpResponse
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

@login_required
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
                user = user_form.save(commit=False)
                raw_password = user_form.cleaned_data['password']
                user.set_password(raw_password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                registered = True
                messages.success(request, "Registrazione completata. Effettua il login.")
                return redirect('todo_list:user_login')
            except Exception as exc:
                messages.error(request, f"Errore durante la registrazione: {exc}")
        else:
            messages.error(request, "Controlla i campi evidenziati e riprova.")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(
        request,
        'todo_list/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    )

        
       
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                next_url = request.GET.get("next") or reverse("todo_list:index")
                return redirect(next_url)
            messages.error(request, "Account non attivo. Contatta l'amministratore.")
        else:
            messages.error(request, "Credenziali non valide. Riprova.")

    return render(request, 'todo_list/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Sei stato disconnesso correttamente.")
    return render(request, 'todo_list/logout.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")
