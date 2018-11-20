from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer, CategoryListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Category.objects.all()

    def get_serializer_class(self):
        return CategoryListSerializer if self.action == 'list' else CategorySerializer
