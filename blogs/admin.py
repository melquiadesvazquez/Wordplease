from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ['id', 'owner', 'slug']
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title', 'description']
