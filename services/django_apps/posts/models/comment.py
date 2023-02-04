from django.db.models import QuerySet
from django_apps.posts.models import Comment, Post


def get_all_comments_by_post(post: Post | int) -> QuerySet[Comment]:

    if isinstance(post, int):
        post = Post.objects.get(id=post)

    result = get_comments_by_post(post=post)
    return result


def get_last_comment_by_post(post: Post) -> Comment:
    return get_comments_by_post(post=post).last()


def get_comments_by_post(post: Post) -> QuerySet[Comment]:
    return Comment.objects.select_related('post')

