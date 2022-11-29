from django.contrib import admin
from .models import Products



@admin.register(Products)
class ProcuctsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stack')
    search_fields = ('name', 'title')
    list_filter = ('update',)
    prepopulated_fields = {'slug':('title',)}

