from django import forms
from django.contrib import admin
from .models import *


class ColorForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={'type': 'color'}),
        }


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'code']
    form = ColorForm


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ComputerModel)
class ComputerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'price', 'created_at']
    list_filter = ['category', 'brand', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['category', 'brand']


@admin.register(AccessoriesModel)
class AccessoriesComModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'price', 'created_at']
    list_filter = ['category', 'brand', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['category', 'brand']
