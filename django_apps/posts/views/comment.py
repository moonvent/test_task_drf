from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django_apps.posts.models import Comment, Post
from django_apps.posts.pagination import CommentPagination, PostsPagination
from django_apps.posts.permissions import IsOwnerOrReadOnly
from django_apps.posts.serializers import CommentSerializer, PostSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.request.parser_context['kwargs'].get('post_id'))


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

