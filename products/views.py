from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.views.generic.list import ListView
from basket.models import Basket
from .models import Product, Product_category

class ProductsView(ListView):
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 2
    
    def get_queryset(self):
        if self.kwargs['category'] != "all":
            return get_list_or_404(Product, category__pk=Product_category.objects.get(name=self.kwargs['category']).id)
        else:
            return get_list_or_404(Product)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Продукты'
        context["categorys"] = Product_category.objects.all()
        context["basket"] = Basket.objects.filter(user=self.request.user).first() if self.request.user.is_authenticated else None
        context["active"] = self.kwargs['category']
        return context

def productPersonal(request, category, pk):
    product = get_object_or_404(Product, id=pk)
    basket = None
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
    return render(request, 'products/personal.html', {'title': 'Продукты','product': product, 'basket': basket})