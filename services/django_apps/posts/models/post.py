from django.db.models import F
from django_apps.posts.models import Post


def add_view_point(post: Post):
    Post.objects.filter(id=post.id).update(views=F('views') + 1)

    # not correct method
    # post.views += 1
    # post.save()
