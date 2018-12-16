from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Grands permissions if superuser or any user doing 'create', 'retrieve', 'update', 'destroy'
        """
        return view.action == 'create' or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """
        Grands permissions if superuser or authenticated user is doing the previous actions on himself
        """
        return request.user.is_superuser or request.user == obj
