from django.db import models


class Todo(models.Model):
    TASK_STATUS = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=30, choices=TASK_STATUS, default='PENDING')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    
    
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    

    