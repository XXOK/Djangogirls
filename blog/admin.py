from django.contrib import admin
from blog.models import Post, Comment, Place

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['post_id', 'id', 'post', 'comment']


@admin.register(Place)
class MapAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']