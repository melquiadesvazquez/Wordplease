from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    permission_classes = [PostPermission]
    queryset = Post.objects.all()

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'owner__first_name', 'owner__last_name']
    ordering = ['id', 'price', 'status', 'name', 'pub_date', 'last_modification']
    filter_fields = ['status', 'owner', 'price']

    def get_queryset(self):
        return self.queryset if self.request.user.is_authenticated else self.queryset.filter(status=Post.PUBLISHED)

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
