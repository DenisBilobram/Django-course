from django.db import models
from django.contrib.auth.models import AbstractUser

class ModUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

