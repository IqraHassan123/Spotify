from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsArtist(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'artist'


class IsDistributor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'distributor'


class IsRecordLabel(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'record_label'
