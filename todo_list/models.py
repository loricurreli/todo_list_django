from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    TASK_STATUS = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=30, choices=TASK_STATUS, default='PENDING')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
    
    
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,  on_delete=models.CASCADE, related_name='profile' )
    
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username
