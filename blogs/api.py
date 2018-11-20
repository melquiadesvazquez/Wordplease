from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from blogs.models import Blog
from blogs.permissions import BlogPermission
from blogs.serializers import BlogSerializer, BlogListSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    permission_classes = [BlogPermission]
    queryset = Blog.objects.all()

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description', 'owner__username', 'owner__first_name', 'owner__last_name']
    ordering = ['title']
    filter_fields = ['owner']

    def get_serializer_class(self):
        return BlogListSerializer if self.action == 'list' else BlogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
