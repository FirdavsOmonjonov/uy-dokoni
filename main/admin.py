from django.contrib import admin
from django.utils.safestring import  mark_safe
from .models import Category, Home

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' )
    list_display_links = ('id', 'name' )

    prepopulated_fields ={'slug': ('name', )}

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'get_image')
    list_display_links = ('id', 'description')

    def get_image(sels, home):
        return mark_safe(f'<img src="{home.image.url}" width="50" height="50" />')

    
