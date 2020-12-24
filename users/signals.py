# from users.models import Profile, Activation
# from django.contrib.auth.models import User
# from django.db.models.signals import pre_save, post_save
# import random, hashlib
# from django.dispatch import receiver

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         instance.is_active = False
#         salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
#         activation_key = hashlib.sha1((instance.email + salt).encode('utf8')).hexdigest()
#         Activation.objects.create(user=instance, activation_key=activation_key)
#         instance.save()

# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)