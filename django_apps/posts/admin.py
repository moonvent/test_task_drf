from django.contrib import admin

from django_apps.posts.models import Comment, Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'text',
                    'views',
                    'creation_date')
    search_fields = ('title',
                     'text',
                     'creation_date')


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('id',
                    'post_title',
                    'text',
                    'creation_date')
    search_fields = ('post__title',
                     'text',
                     'creation_date')
    autocomplete_fields = ('post',
                           )
