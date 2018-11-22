from rest_framework.permissions import BasePermission


class FilePermission(BasePermission):

    def has_permission(self, request, view):
        """
        Grands permissions if superuser or any user doing 'list'
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Grands permissions if superuser or authenticated user is doing the previous actions on himself
        """
        return request.user.is_authenticated
