from rest_framework import permissions

class AllowPostFromUnregisteredUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False