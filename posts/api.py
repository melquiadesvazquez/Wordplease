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
    queryset = Post.objects.all().order_by('-pub_date')

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description', 'author__username', 'author__first_name', 'author__last_name']
    ordering = ['id', 'title', 'status', 'pub_date']
    filter_fields = ['status', 'author', 'title', 'category']

    def get_queryset(self):
        return self.queryset if self.request.user.is_authenticated else self.queryset.filter(status=Post.PUBLISHED)

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
