from rest_framework import permissions
from rest_framework.permissions import BasePermission


class HasPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            return obj.is_owner(request.user)
