from django.db import models

class Product_category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField(default=100)
    image = models.ImageField(upload_to='product_images', blank=True)
    price = models.IntegerField(default=100)
    category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
