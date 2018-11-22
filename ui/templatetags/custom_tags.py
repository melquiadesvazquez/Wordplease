import six
from django import template

from categories.models import Category

register = template.Library()


@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, six.string_types):
        return text.startswith(starts)
    return False


@register.simple_tag
def get_categories():
    return Category.objects.all()

