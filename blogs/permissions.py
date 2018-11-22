from rest_framework.permissions import BasePermission


class BlogPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Grands permissions if superuser or any user doing 'list', 'create'
        """
        return view.action in ('list', 'create') or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Grands permissions if superuser or authenticated user is doing the previous any action on himself
        """
        return obj.owner == request.user or request.user.is_superuser
