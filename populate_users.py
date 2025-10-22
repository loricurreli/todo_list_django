import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

from todo_list.models import User
from faker import Faker
fakegen = Faker()


def populate(N=5):

    for entry in range(N):
        first_name=fakegen.first_name()
        last_name=fakegen.last_name()
        email=fakegen.email()
        todo, created = User.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email
       )


if __name__ == '__main__':
    print("Populating users!")
    populate(20)
    print("Populating complete!")