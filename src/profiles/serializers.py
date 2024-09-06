from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """displaying information the user"""
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class GetUserPublicSerializer(serializers.ModelSerializer):
    """displaying information to the public user"""

    class Meta:
        model = UserNet
        exclude = (
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )
