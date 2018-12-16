from rest_framework.permissions import BasePermission


class CategoryPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Grands permissions if superuser or any user doing 'list'
        """
        return view.action in ('list', 'retrieve') or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Grands permissions if superuser or authenticated user is doing the previous actions on himself
        """
        return view.action == 'retrieve' or request.user.is_authenticated or request.user.is_superuser
