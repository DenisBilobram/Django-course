from users.models import ModUser, ModUserProfile
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(post_save, sender=ModUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ModUserProfile.objects.create(user=instance)


@receiver(post_save, sender=ModUser)
def save_user_profile(sender, instance, **kwargs):
    instance.moduserprofile.save()