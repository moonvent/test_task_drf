import os
from django.contrib import admin
from django.urls import include, path
from django_apps.posts.views import post, comment


urlpatterns = [
    path('', post.PostList.as_view()),
    path('<int:pk>/', post.PostDetail.as_view()),

    path('comments_by_post/<int:post_id>/', comment.CommentList.as_view()),
    path('comment/<int:pk>/', comment.CommentDetail.as_view()),
]

