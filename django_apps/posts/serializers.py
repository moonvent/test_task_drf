from django.contrib.admin.utils import lookup_field
from django.contrib.auth.models import User
from rest_framework import serializers

from django_apps.posts.models import Comment, Post
from services.constants import COMMENT_NOT_EXISTS, RETURN_ALL_COMMENTS_FLAG
from services.django_apps.posts.models.comment import get_all_comments_by_post
from services.django_apps.posts.views.post import get_last_comment_data


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('views',)

    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.SlugRelatedField(many=True, slug_field='text', read_only=True)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'posts')

