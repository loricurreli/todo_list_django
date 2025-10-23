from django.urls import path

from . import views

app_name = 'todo_list'

urlpatterns = [
    path("todos/", views.index, name="index"),
    path("register/", views.register, name="register"),
    # path("users/", views.users, name="users"),
    path("new_task/", views.new_task, name="new_task"),
    path("logout/", views.user_logout, name="logout"),
    path("login/", views.user_login, name="user_login"),
    path("special/", views.special, name='special')
]