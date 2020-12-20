from .models import ModUser
from django.contrib.auth import forms

class UserLoginForm(forms.AuthenticationForm):
    class Meta():
        model = ModUser
        fields = ('username', 'password')

class UserRegistrForm(forms.UserCreationForm):
    class Meta():
        model = ModUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'age', 'avatar')

class UserEditForm(forms.UserChangeForm):
    class Meta():
        model = ModUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar')