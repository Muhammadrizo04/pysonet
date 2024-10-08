from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from src.wall.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts"""
    list_display = ("user", "published", "create_date", "moderation", "view_count", "id")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """comments post"""
    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    # actions = ['unpublished', 'publish']
    mptt_level_indent = 15
