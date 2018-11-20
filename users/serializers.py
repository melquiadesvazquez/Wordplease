from django.contrib.auth.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class UserSerializer(UserListSerializer):

    class Meta(UserListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['id', 'date_joined']



