from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.role == 'ADMIN':
                return redirect('/admin-dashboard/')

            elif user.role == 'STUDENT':
                return redirect('/student-dashboard/')

            elif user.role == 'COUNSELOR':
                return redirect('/counselor-dashboard/')

        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def manage_users(request):
    if request.user.role != 'ADMIN':
        return redirect('/')

    if request.method == 'POST':

        if request.POST.get('action') == 'create':
            User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                role=request.POST.get('role')
            )

        elif request.POST.get('action') == 'update':
            user = User.objects.get(
                id=request.POST.get('user_id')
            )

            user.role = request.POST.get('role')
            user.save()

        elif request.POST.get('action') == 'delete':
            user = User.objects.get(
                id=request.POST.get('user_id')
            )

            user.delete()

        return redirect('/accounts/manage-users/')

    users = User.objects.all().order_by('id')

    context = {
        'users': users
    }

    return render(
        request,
        'manage_users.html',
        context
    )