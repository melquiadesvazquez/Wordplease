from rest_framework import viewsets

from blogs.models import Blog
from blogs.serializers import BlogSerializer, BlogListSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        return BlogListSerializer if self.action == 'list' else BlogSerializer
