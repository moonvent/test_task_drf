import os
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django_apps.posts.views import post, comment


urlpatterns = [
    # path('posts/', lambda request: redirect('post_list')),
    path('posts/', post.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', post.PostDetail.as_view(), name='post_detail'),
    # path('posts/create/', post.PostCreate.as_view(), name='post_create'),

    path('post_comments/<int:post_id>/', comment.CommentList.as_view()),
    path('comments/<int:pk>/', comment.CommentDetail.as_view()),
]

