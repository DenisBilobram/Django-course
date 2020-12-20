from basket.models import Basket
from django.shortcuts import render

def indexView(request):
    basket = None
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
    return render(request, 'mainapp/index.html', {'title': 'Магазин', 'basket': basket})

def contactView(request):
    basket = None
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
    return render(request, 'mainapp/contact.html', {'title': 'Контакты', 'basket': basket})

def not_found(request, exception):
    return render(request, 'mainapp/404.html', status=404)
