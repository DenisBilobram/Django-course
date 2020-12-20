from django.urls import path
from .views import basket, basketAdd, basketDelete
app_name = 'basket'

urlpatterns = [
    path('', basket, name='index'),
    path('add/<int:pk>', basketAdd, name='add'),
    path('delete/<int:pk>', basketDelete, name='delete'),
]
