from django.urls import path
from .views import indexView, contactView

app_name = 'mainapp'

urlpatterns = [
    path('', indexView, name='index'),
    path('contact', contactView, name='contact'),
]
