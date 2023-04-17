from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Movie)
class MOovieModelAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'description', 'genre')


@admin.register(Collection)
class CollectionModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description')