from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Grands permissions if superuser or any user doing 'create', 'retrieve', 'update', 'destroy'
        """
        return request.user.is_superuser or view.action in ['create', 'retrieve', 'update', 'destroy']

    def has_object_permission(self, request, view, obj):
        """
        Grands permissions if superuser or authenticated user is doing the previous actions on himself
        """
        return request.user.is_superuser or request.user == obj
