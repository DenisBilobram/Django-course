from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.forms import ModelForm
import random, hashlib

class UserLoginForm(forms.AuthenticationForm):
    class Meta():
        model = User
        fields = ('username', 'password')

class UserRegistrForm(forms.UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')


class UserEditForm(forms.UserChangeForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('tagline', 'aboutMe', 'gender', 'age', 'avatar')