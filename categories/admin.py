from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    readonly_fields = ['slug']
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'slug']


