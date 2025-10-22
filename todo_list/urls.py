from django.urls import path

from . import views

urlpatterns = [
    path("todos/", views.index, name="index"),
    path("users/", views.users, name="users"),
    path("new_task/", views.new_task, name="new_task"),
]