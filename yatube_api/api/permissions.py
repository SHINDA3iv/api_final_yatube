from rest_framework import permissions


# Проверка прав доступа
class OwnershipPermission(permissions.BasePermission):

    # Разрешение на уровне запроса
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    # Разрешение на уровне объекта
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
