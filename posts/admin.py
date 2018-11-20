from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):

    readonly_fields = ['slug']
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title', 'description']
