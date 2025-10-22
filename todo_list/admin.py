from django.contrib import admin
from todo_list.models import Todo, User

admin.site.register(Todo)
admin.site.register(User)