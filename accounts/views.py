from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group


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



from django.contrib.auth.models import User, Group

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']

        if password1 != password2:
            return render(request, 'accounts/register.html', {
                'error': 'Les mots de passe ne correspondent pas.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Ce nom d\'utilisateur existe déjà.'
            })

        user = User.objects.create_user(username=username, password=password1)
        group = Group.objects.get(name=role)
        user.groups.add(group)
        user.save()
        login(request, user)
        messages.success(request, f'Bienvenue {user.username} !')
        return redirect('index')

    return render(request, 'accounts/register.html')