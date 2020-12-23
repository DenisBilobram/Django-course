from django.core.management.base import BaseCommand, CommandError
from users.models import ModUser, ModUserProfile

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ModUser.objects.all()
        for user in users:
            user_profile = ModUserProfile.objects.create(user=user)
            user_profile.save()
