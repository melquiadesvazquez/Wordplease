from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm


class UserForm(ModelForm):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
