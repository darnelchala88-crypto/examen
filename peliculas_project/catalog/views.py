from django.shortcuts import render, redirect # pyright: ignore[reportMissingModuleSource]
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout # pyright: ignore[reportMissingModuleSource]
from django.contrib import messages # pyright: ignore[reportMissingModuleSource]
from django.contrib.auth.forms import AuthenticationForm # pyright: ignore[reportMissingModuleSource]
from django.contrib.auth.decorators import login_required # pyright: ignore[reportMissingModuleSource]
from .forms import UserRegisterForm, MovieForm
from .models import Movie

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada correctamente. Ahora entra con tu usuario.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'catalog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('movie_list')
    else:
        form = AuthenticationForm()
    return render(request, 'catalog/login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'catalog/movie_form.html', {'form': form})

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'catalog/movie_list.html', {'movies': movies})
