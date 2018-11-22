from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):

    readonly_fields = ['pub_date', 'last_modification', 'id', 'slug', 'image_tag']
    list_display = ['title', 'description', 'image', 'video', 'formatted_pub_date', 'formatted_last_modification']
    list_filter = ['status', 'author', 'title', 'category']
    search_fields = ['title', 'description', 'author__username', 'author__first_name', 'author__last_name']


    def image_tag(self, obj):
        src = "https://picsum.photos/200/200/?image=1027"
        if obj.image:
            if obj.image.name.startswith('https://picsum.photos'):
                src = obj.image.name
            else:
                src = obj.image.url

        return mark_safe(
            '<img src="{0}" alt="{1}" title="{1}" width="auto" height="100">'.format(src, obj.title)
        )

    image_tag.short_description = 'Image preview'

    def formatted_pub_date(self, obj):
        return obj.pub_date.strftime('%d/%m/%Y %H:%M')

    formatted_pub_date.short_description = 'Pub date'
    formatted_pub_date.admin_order_field = 'pub_date'

    def formatted_last_modification(self, obj):
        return obj.last_modification.strftime('%d/%m/%Y %H:%M')

    formatted_last_modification.short_description = 'Las modification date'
    formatted_last_modification.admin_order_field = 'last_modification'

    fieldsets = [
        [None, {
            'fields': ['image_tag', 'image', 'title', 'description', 'content']
        }],
        ['Post meta', {
            'fields': ['author', 'blog', 'category', 'status'],
            'description': 'Info related with post and more...',
        }],
        ['Post dates', {
            'fields': ['pub_date', 'last_modification'],
            'classes': ['collapse']
        }]
    ]
