from rest_framework import permissions
from .models import Teacher


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Teacher.objects.filter(user=request.user)
    

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if not Teacher.objects.filter(user=request.user).exists():
            if not request.user.is_staff and request.user.is_superuser:
                return True


class IsAuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated 