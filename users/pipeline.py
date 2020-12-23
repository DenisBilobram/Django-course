from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from users.models import ModUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    ModUserProfile.objects.create(user=user)
    profile = ModUserProfile.objects.get(user=user)
    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        if data['sex'] == 1:
            profile.gendre = ModUserProfile.FEMALE
        if data['sex'] == 2:
            profile.gender = ModUserProfile.MALE

    if data['about']:
        profile.aboutMe = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        user.age = age
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    
    profile.save()
    user.save()

    

