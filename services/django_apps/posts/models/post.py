from django_apps.posts.models import Post


def add_view_point(post: Post):
    post.views += 1
    post.save()
