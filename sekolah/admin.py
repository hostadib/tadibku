from django.contrib import admin

#from django.contrib import admin
from .models import Sma

@admin.register(Sma)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug' : ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']