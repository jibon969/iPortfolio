from django.contrib import admin
from .models import Category, Blog, Comment, Reply


class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = Blog


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'email']
    search_fields = ['name', 'email']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name',]
    search_fields = ['name']

    class Meta:
        model = Reply


admin.site.register(Reply, ReplyAdmin)