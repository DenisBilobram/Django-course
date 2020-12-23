from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

class ModUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True, default=18)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now()+timedelta(hours=48)))
    
    def is_activation_key_good(self):
        if now() <= self.activation_key_expires:
            return True
        else:
            return False

class ModUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    user = models.OneToOneField(ModUser, unique=True, null=False,\
                                db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, \
                               blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, \
                               blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, \
                              choices=GENDER_CHOICES, blank=True)