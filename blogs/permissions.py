from rest_framework.permissions import BasePermission


class BlogPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Grands permissions if superuser or any user doing 'create', 'retrieve', 'update', 'destroy'
        """
        return view.action in ('list', 'create', 'retrieve', 'update', 'destroy') or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Grands permissions if superuser or authenticated user is doing the previous actions on himself
        """
        return view.action == 'retrieve' or obj.owner == request.user or request.user.is_superuser
