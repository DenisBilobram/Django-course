from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.forms import UserRegistrForm, UserEditForm
from products.forms import ProductCreateForm
from users.models import ModUser
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from products.models import Product

title = 'Admin'

@user_passes_test(lambda u: u.is_staff)
def adminview(request):
    return render(request, 'adminapp/base.html', {'title': title})

class UsersView(ListView):
    model = ModUser
    template_name = 'adminapp/list.html'
    context_object_name = 'users_detail'
    paginate_by = 2

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UsersPersonal(DetailView):
    model = ModUser
    template_name = 'adminapp/detail.html'
    context_object_name = 'user_detail'
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class UsersCreate(CreateView):
    model = ModUser
    template_name = 'adminapp/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('adminapp:users')
    form_class = UserRegistrForm
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class UsersEdit(UpdateView):
    model = ModUser
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('adminapp:users')
    context_object_name = 'form'
    form_class = UserEditForm
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UsersDelete(DeleteView):
    model = ModUser
    template_name = 'adminapp/delete.html'
    success_url = reverse_lazy('adminapp:users')
    context_object_name = "user_detail"
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
        
class ProdcutsView(ListView):
    model = Product
    template_name = 'adminapp/list.html'
    context_object_name = 'products'
    paginate_by = 2
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ProductsPersonal(DetailView):
    model = Product
    template_name = 'adminapp/detail.html'
    context_object_name = 'product_detail'
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
        
class ProductsCreate(CreateView):
    model = Product
    template_name = 'adminapp/create.html'
    success_url = reverse_lazy('adminapp:products')
    form_class = ProductCreateForm
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
        
class ProductsEdit(UpdateView):
    model = Product
    template_name = 'adminapp/edit.html'
    success_url = reverse_lazy('adminapp:products')
    form_class = ProductCreateForm
    context_object_name = 'form'
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ProductsDelete(DeleteView):
    model = Product
    template_name = 'adminapp/delete.html'
    success_url = reverse_lazy('adminapp:products')
    context_object_name = 'product'
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)