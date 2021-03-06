from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from .forms import OrderForm, OrderItemForm
from .models import Order, OrderItem
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from basket.models import Basket
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete
from products.models import Product
from django.http import JsonResponse

class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class OrderCreateView(View):
    def get(self, request):
        OrderFormSet = inlineformset_factory(Order, OrderItem, \
                                            form=OrderItemForm, extra=1)
        basket_items = Basket.objects.filter(user=self.request.user)
        formset = OrderFormSet()
        if len(basket_items):
            OrderFormSet = inlineformset_factory(Order, OrderItem, \
                                form=OrderItemForm, extra=len(basket_items))
            formset = OrderFormSet()
            for num, form in enumerate(formset.forms):
                form.initial['product'] = basket_items[num].product
                form.initial['quantity'] = basket_items[num].quantity
                form.initial['price'] = basket_items[num].product.price * basket_items[num].quantity
        return render(request, "ordersapp/order_form.html", {"orderitems": formset})

    def post(self, request):
        OrderFormSet = inlineformset_factory(Order, OrderItem, \
                                        form=OrderItemForm, extra=1)
        order = Order.objects.create(user=request.user)
        formset = OrderFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
        if order.get_total_cost() == 0:
            order.delete()
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            basket_items.delete()
        return redirect('ordersapp:list')

class OrderUpdateView(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('ordersapp:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, 
                                     OrderItem, 
                                     form=OrderItemForm, 
                                     extra=1)
        if self.request.POST:
            data['orderitems'] = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset.forms:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price * form.instance.quantity
            data['orderitems'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

       # удаляем пустой заказ
        if self.object.get_total_cost() == 0:
            self.object.delete()
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:list')

class OrderRead(DetailView):
   model = Order

   def get_context_data(self, **kwargs):
       context = super(OrderRead, self).get_context_data(**kwargs)
       context['title'] = 'заказ/просмотр'
       return context

def order_forming_complete(request, pk):
   order = get_object_or_404(Order, pk=pk)
   order.status = Order.SENT_TO_PROCEED
   order.save()
   return redirect('ordersapp:list')

@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(sender, update_fields, instance, **kwargs):
   if update_fields is 'quantity' or 'product':
       if instance.pk:
           instance.product.quantity -= instance.quantity - \
                                        sender.objects.get(id=instance.pk).quantity
       else:
           instance.product.quantity -= instance.quantity
       instance.product.save()


@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_delete(sender, instance, **kwargs):
   instance.product.quantity += instance.quantity
   instance.product.save()


def ProdctsAjaxHandler(reqeust):
    if reqeust.is_ajax():
        product_name = reqeust.GET.get('product_name')
        product = Product.objects.get(name=product_name)
        price = product.price
        return JsonResponse({'price': price}, status=200)