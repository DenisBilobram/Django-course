from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
from datetime import timedelta

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, null=False,\
                                db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=128, blank=True)
    aboutMe = models.TextField(max_length=512, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField(default=18, blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

class Activation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, null=False,\
                                db_index=True, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now()+timedelta(hours=48)))

    def is_activation_key_good(self):
        if now() <= self.activation_key_expires:
            return True
        else:
            return False