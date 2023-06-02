from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from .models import CustomUser

class IsAdminCustomUser(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.role_id == 1:
            return True
        return False
    
class HasOrganization(BasePermission):
    def has_permission(self, request, view):
        if request.user.organization_id is not None:
            return True
        return False

class CustomObjectPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Ваша логика проверки разрешений для конкретного объекта
        return True  # Или False

class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

