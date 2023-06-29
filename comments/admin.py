from django.contrib import admin
from .models import Comment, Replay


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'active', 'created_at', 'updated_at']
    list_editable = ['active']
    search_fields = ['name', 'email', 'body']


@admin.register(Replay)
class ReplayAdmin(admin.ModelAdmin):
    list_display = ['post', 'body', 'created_at', 'updated_at']
    search_fields = ['body']
