from django.shortcuts import render, redirect
from .forms import UserRegistrForm, UserEditForm, ModUserProfileEditForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import auth
from .models import ModUser

def RegistrView(request):
    form = UserRegistrForm()
    if request.method == 'POST':
        form = UserRegistrForm(request.POST, request.FILES)
        if form.is_valid():
            # form.instance.is_active = False
            user = form.save()
            if send_verify_mail(user):
                print('succes')
            else:
                print('error') 
            return redirect('mainapp:index')
    return render(request, 'users/registr.html', {'title': 'Registration', 'form': form})

def EditView(request):
    form = UserEditForm(instance=request.user)
    profile_form = ModUserProfileEditForm(instance=request.user.moduserprofile)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        profile_form = ModUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return redirect('users:edit')
    return render(request, 'users/edit.html', {'title': 'Edit', 'form': form, 'profile_form': profile_form})

def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

def verify(request, email, activation_key):
    try:
        user = ModUser.objects.get(email=email)
        if user.activation_key == activation_key and user.is_activation_key_good():
            user.activation_key = ''
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'users/verification.html')
    except Exception as error:
        print(error)
