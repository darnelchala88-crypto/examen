from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Movie

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'director', 'release_date', 'description']
