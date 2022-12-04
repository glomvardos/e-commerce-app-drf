from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'ADMIN'


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'CUSTOMER'


class DenyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'ADMIN'
