import six
from django import template

register = template.Library()


@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, six.string_types):
        return text.startswith(starts)
    return False
