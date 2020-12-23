from .models import ModUser, ModUserProfile
from django.contrib.auth import forms
from django.forms import ModelForm
import random, hashlib

class UserLoginForm(forms.AuthenticationForm):
    class Meta():
        model = ModUser
        fields = ('username', 'password')

class UserRegistrForm(forms.UserCreationForm):
    class Meta():
        model = ModUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def save(self):
            user = super().save()
            user.is_active = False
            salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
            user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
            user.save()
            return user

class UserEditForm(forms.UserChangeForm):
    class Meta():
        model = ModUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar')

class ModUserProfileEditForm(ModelForm):
    class Meta:
        model = ModUserProfile
        fields = ('tagline', 'aboutMe', 'gender')