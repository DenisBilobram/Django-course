from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen
from .forms import ProfileEditForm
import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from users.models import Profile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
        
    profile, created = Profile.objects.get_or_create(user=user)

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_400_orig')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    
    
    if created:
        data = resp.json()['response'][0]
        if data['sex']:
            if data['sex'] == 1:
                profile.gendre = Profile.FEMALE
            if data['sex'] == 2:
                profile.gender = Profile.MALE

        if data['about']:
            profile.aboutMe = data['about']

        if data['bdate']:
            bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
            age = timezone.now().date().year - bdate.year
            user.profile.age = age
            if age < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        avatar = urlopen(data['photo_400_orig']).read()
        out = open(f"media\\users_avatars\\{response['id']}.jpg", "wb")
        out.write(avatar)
        out.close
        profile.avatar = f"users_avatars/{response['id']}.jpg"
        # profile_form = ProfileEditForm(instance=user.profile, avatar=avatar)


    profile.save()
    user.save()

    

