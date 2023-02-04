from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django_apps.posts.models import Post
from django_apps.posts.pagination import PostsPagination
from django_apps.posts.permissions import IsOwnerOrReadOnly
from django_apps.posts.serializers import CommentSerializer, PostSerializer
from services.constants import RETURN_ALL_COMMENTS_FLAG
from services.django_apps.posts.models.post import add_view_point
from services.django_apps.posts.views.post import get_comments_data_for_one_post


class PostList(generics.ListAPIView):
    queryset = Post.objects.prefetch_related('comments').all()
    serializer_class = PostSerializer
    pagination_class = PostsPagination

    def list(self, request):
        queryset = (Post
                    .objects
                    .prefetch_related('comments')
                    .prefetch_related('owner')
                    .all())
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    
class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_serializer(self, *args, **kwargs):
        serializer: PostSerializer = super(PostDetail, self).get_serializer(*args, **kwargs)
        serializer.context.update({RETURN_ALL_COMMENTS_FLAG: 1})
        add_view_point(self.get_object())
        # serializer.data.last_comment = get_comments_data_for_one_post(post=self.get_object())
        return serializer

