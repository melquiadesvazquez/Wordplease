from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, PostPermission]
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'author__first_name', 'author__last_name']
    ordering = ['id', 'title', 'status', 'pub_date', 'last_modification']
    filter_fields = ['status', 'author', 'title']

    def get_queryset(self):
        return self.queryset if self.request.user.is_authenticated else self.queryset.filter(status=Post.PUBLISHED)

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False)
    def me(self, request):
        posts = Post.objects.filter(author=request.user)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
