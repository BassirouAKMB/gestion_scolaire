from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} !')
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'Identifiants incorrects'})
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Déconnexion réussie.')
    return redirect('login')