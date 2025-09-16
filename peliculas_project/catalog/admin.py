from django.contrib import admin # type: ignore
from .models import Movie

admin.site.register(Movie)
