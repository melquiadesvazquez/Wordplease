from django.forms import ModelForm

from blogs.models import Blog
from posts.models import Post


class PostForm(ModelForm):

    class Meta:

        model = Post
        fields = ['blog', 'category', 'title', 'description', 'content', 'image', 'video', 'status']

        error_messages = {
            'title': {
                'max_length': "The title is too long.",
            },
        }

    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(owner=user)
