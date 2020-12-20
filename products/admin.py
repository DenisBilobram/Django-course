from django.contrib import admin
from .models import Product, Product_category

admin.site.register(Product_category)
admin.site.register(Product)
