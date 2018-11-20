from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Post.objects.all()

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer
