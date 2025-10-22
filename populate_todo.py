import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

from todo_list.models import Todo
from faker import Faker
fakegen = Faker()


def populate(N=5):

    for entry in range(N):
        title=fakegen.text(30)
        status="Pending"
        description=fakegen.text(250)
        todo, created = Todo.objects.get_or_create(
            title=title,
            status=status,
            description=description
       )


if __name__ == '__main__':
    print("Populating todos!")
    populate(20)
    print("Populating complete!")