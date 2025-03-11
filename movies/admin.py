from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie_id', 'file_id')
    search_fields = ('title', 'movie_id')

