from django.contrib.admin.utils import lookup_field
from django.contrib.auth.models import User
from rest_framework import serializers

from django_apps.posts.models import Comment, Post
from services.constants import COMMENT_NOT_EXISTS


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('views',)

    owner = serializers.ReadOnlyField(source='owner.username')
    last_comment = serializers.SerializerMethodField()

    def get_last_comment(self, 
                         post: Post):
        query_set = Comment.objects.filter(post=post).order_by('-id')[:1]
        comments = CommentSerializer(query_set, many=True, read_only=True).data
        return comments[0] if comments else COMMENT_NOT_EXISTS


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
