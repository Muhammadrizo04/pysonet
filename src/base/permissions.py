from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsMemberGroup(BasePermission):
    """ Group member or administrator """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.group.members.all() or obj.group.founder == request.user


class IsAuthorEntry(BasePermission):
    """ Author of the post or administrator """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or obj.group.fouder == request.user


class IsAuthorCommentEntry(BasePermission):
    """ Comment author or administrator """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or obj.entry.group.founder == request.user


class IsAuthor(BasePermission):
    """ Author of the comment or post """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
