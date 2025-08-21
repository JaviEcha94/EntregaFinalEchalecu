from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'rating')
    search_fields = ('title', 'genre', 'rating')
    list_filter = ('genre', 'rating', 'year')
