from rest_framework import permissions

from accounts.models import User

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            user = User.objects.get(username=request.user)
            return user.is_superuser
