from basket.models import Basket
from django.shortcuts import render

def indexView(request):
    return render(request, 'mainapp/index.html', {'title': 'Магазин'})

def contactView(request):
    return render(request, 'mainapp/contact.html', {'title': 'Контакты'})

def not_found(request, exception):
    return render(request, 'mainapp/404.html', status=404)
