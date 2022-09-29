from rest_framework.permissions import BasePermission

from apps.accounts.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.access_level == User.AccessLevel.ADMIN


class IsPlayer(BasePermission):
    def has_permission(self, request, view):
        return request.user.access_level == User.AccessLevel.PLAYER
