from django.contrib import admin
from .models import Blogger, Blog, Comment

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    fields = ['name', 'bio']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'author', 'description')
    fields = ['title', 'post_date', 'author', 'description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'comment_date', 'comment')
    fields = ['author', 'blog', 'comment']