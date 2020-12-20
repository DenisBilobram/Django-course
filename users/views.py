from django.shortcuts import render, redirect
from .forms import UserRegistrForm, UserEditForm

def RegistrView(request):
    form = UserRegistrForm()
    if request.method == 'POST':
        form = UserRegistrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:index')
    return render(request, 'users/registr.html', {'title': 'Registration', 'form': form})

def EditView(request):
    form = UserEditForm(instance=request.user)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:edit')
    return render(request, 'users/edit.html', {'title': 'Edit', 'form': form})