import os
from django.contrib import admin
from django.urls import include, path
from django_apps.posts.views import post, comment


urlpatterns = [
    path('posts/', post.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', post.PostDetail.as_view(), name='post_detail'),

    path('post_comments/<int:post_id>/', comment.CommentList.as_view()),
    path('comments/<int:pk>/', comment.CommentDetail.as_view()),
]

