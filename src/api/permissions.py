from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of the object to edit it.
    """
    def has_object_permission(self,request, view, obj):
        # Read permission is allowed to any object.
        # GET, HEAD or OPTIONS requests are always allowed.

        if requests.method in permission.SAFE_METHODS:
            return True

        # Write permission is only allowed to the owner of the object.
        return obj.owner == request.user
