from rest_framework.permissions import BasePermission

from posts.models import Post


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Grands permissions if superuser or any user doing 'list', 'create'
        """
        return view.action in ('list', 'retrieve') or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Grands permissions if superuser or authenticated user is doing the previous actions on himself
        """
        return (obj.status == Post.PUBLISHED and view.action == 'retrieve') or obj.author == request.user or request.user.is_superuser
