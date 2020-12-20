from django.urls import path
from .views import ProductsView, productPersonal

app_name = 'products'

urlpatterns = [
    path('<str:category>/', ProductsView.as_view(), name='category'),
    path('<str:category>/<int:page>', ProductsView.as_view(), name='page'),
    path('<str:category>/personal/<int:pk>', productPersonal, name='personal'),
]