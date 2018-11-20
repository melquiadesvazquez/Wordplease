from django.forms import ModelForm

from categories.models import Category


class CategoryForm(ModelForm):

    class Meta:

        model = Category
        fields = ['name', 'description']

        error_messages = {
            'name': {
                'max_length': "The name is too long.",
            },
        }
