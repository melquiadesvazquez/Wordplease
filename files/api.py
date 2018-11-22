from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from files.models import File
from files.permissions import FilePermission
from files.serializers import FileSerializer
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer, PostListSerializer


class FileViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    permission_classes = [FilePermission]
    queryset = File.objects.all()
    serializer_class = FileSerializer

