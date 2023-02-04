from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # use standart user model, cause in tt doesn't describe this part
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    views = models.PositiveIntegerField(help_text='Amount of views',
                                        default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # for select in admin panel post by name
        return self.title


class Comment(models.Model):
    # use standart user model, cause in tt doesn't describe this part
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.CharField(max_length=256)
    creation_date = models.DateTimeField(auto_now_add=True)

    @admin.display(description='Post title')
    def post_title(self):
        # for more comfortable interface understanding, out the post title of comment
        return f'[{self.post.title}]'

    def __str__(self):
        # for select in admin panel comment by post title and a start of comment text
        return f'[{self.post.title}]: {self.text[:50]}...'

