from django.db import models
from django.conf import settings
from products.models import Product

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now=True)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        total = 0
        for item in items:
            total += item.quantity
        return total

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        total = 0
        for item in items:
            total += item.product_cost
        return total
