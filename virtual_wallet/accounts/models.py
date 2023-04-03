from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('Premium', 'Premium'),
        ('Non premium', 'Non premium'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)


