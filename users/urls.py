from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrView, EditView, verify
from .forms import UserLoginForm

app_name = 'users'

urlpatterns = [
    path('login', LoginView.as_view(template_name='users/login.html', authentication_form=UserLoginForm), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registr', RegistrView, name='registr'), 
    path('edit', EditView, name='edit'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]