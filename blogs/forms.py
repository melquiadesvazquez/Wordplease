from django.contrib.auth.models import User
from django.forms import ModelForm

from blogs.models import Blog


class BlogForm(ModelForm):

    class Meta:

        model = Blog
        fields = ['title', 'description']

        error_messages = {
            'title': {
                'max_length': "The title is too long.",
            }
        }
