from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    readonly_fields = ['pub_date', 'last_modification', 'image_tag']
    list_display = ['image_tag', 'title', 'category', 'author_fullname', 'status', 'formatted_pub_date',
                    'formatted_last_modification']
    list_filter = ['status', 'author', 'category']
    search_fields = ['title', 'description', 'author__first_name', 'author__last_name', 'author__username', 'author__email']

    def author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    author_fullname.admin_order_field = 'author__first_name'

    def image_tag(self, obj):
        return mark_safe(
            '<img src="{0}" alt="{1}" title="{1}" width="100" height="100">'.format(obj.image.url, obj.title)
        )

    image_tag.short_description = 'Image'

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
