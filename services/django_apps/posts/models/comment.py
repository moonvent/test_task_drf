from django.db.models import QuerySet
from django_apps.posts.models import Comment, Post


def get_all_comments_by_post(post: Post | int) -> QuerySet[Comment]:

    if isinstance(post, int):
        post = Post.objects.get(id=post)

    return Comment.objects.filter(post=post)


def get_last_comment_by_post(post: Post) -> Comment:
    return Comment.objects.filter(post=post).last()


