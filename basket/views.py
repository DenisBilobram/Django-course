from basket.models import Basket
from products.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def basket(request):
    basket_items = Basket.objects.filter(user=request.user)
    return render(request, 'basket/basket.html', {'baskets': basket_items, 'title': 'Basket'})

@login_required
def basketAdd(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(user=request.user, product=product).first()
    if not basket_item:
        basket_item = Basket(user=request.user, product=product)
    basket_item.quantity += 1
    basket_item.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def basketDelete(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    if not basket_item:
        return redirect(request.META.get('HTTP_REFERER'))
    basket_item.quantity -= 1
    basket_item.save()
    if basket_item.quantity == 0:
        basket_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))
