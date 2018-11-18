from django.contrib import admin
from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ['slug']
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title', 'slug']


