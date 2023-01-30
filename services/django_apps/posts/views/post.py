from django.db.models import QuerySet
from django_apps.posts.models import Comment
from services.constants import COMMENT_NOT_EXISTS
from services.django_apps.posts.models.comment import get_all_comments_by_post, get_last_comment_by_post


def get_comments_data_for_one_post(post, 
                                   only_last_comment: bool = False) -> QuerySet[Comment]:
    """
        Get comments for output in post detail view
    """
    comments = get_all_comments_by_post(post=post)
    return comments.values('id',
                           'owner',
                           'post',
                           'text',
                           'creation_date')


def get_last_comment_data(post) -> str | dict:
    """
        Get last comment for output in post list
    """
    comment = get_last_comment_by_post(post=post)

    result = None

    if not comment:
        result = COMMENT_NOT_EXISTS

    else:
        result = dict(id=comment.id,
                      text=comment.text)

    return result

