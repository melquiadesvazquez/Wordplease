from django.forms import ModelForm

from blogs.models import Blog


class BlogForm(ModelForm):

    class Meta:

        model = Blog
        fields = ['owner', 'title', 'description']

        error_messages = {
            'title': {
                'max_length': "The title is too long.",
            },
        }
