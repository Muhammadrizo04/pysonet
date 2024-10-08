from rest_framework import serializers

from ..base.serializers import RecursiveSerializer, FilterCommentsSerializer
from .models import Post, Comment


class CreateCommentSerializers(serializers.ModelSerializer):
    """Adding comments to a post"""

    class Meta:
        model = Comment
        fields = ("post", "text", "parent")


class ListCommentSerializer(serializers.ModelSerializer):
    """List of comments"""

    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentsSerializer
        model = Comment
        fields = ("id", "post", "user", "text", "created_date", "update_date", "deleted", "children")


class PostSerializer(serializers.ModelSerializer):
    """Output and editing of the post"""
    user = serializers.ReadOnlyField(source='user.username')
    comments = ListCommentSerializer(many=True, read_only=True)
    view_count = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments", "view_count")


class ListPostSerializer(serializers.ModelSerializer):
    """List of posts"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments_count")
