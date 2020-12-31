from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete
from .models import OrderItem
from basket.models import Basket

@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(sender, update_fields, instance, **kwargs):
   if update_fields is 'quantity' or 'product':
       if instance.pk:
           instance.product.quantity -= instance.quantity - \
                                        sender.get_item(instance.pk).quantity
       else:
           instance.product.quantity -= instance.quantity
       instance.product.save()


@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_delete(sender, instance, **kwargs):
   instance.product.quantity += instance.quantity
   instance.product.save()