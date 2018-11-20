from django.contrib.auth.models import User
from rest_framework import viewsets

from users.serializers import UserSerializer, UserListSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserListSerializer if self.action == 'list' else UserSerializer
