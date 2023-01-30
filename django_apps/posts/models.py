from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    views = models.PositiveIntegerField(help_text='Amount of views',
                                        default=0)
    creation_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    creation_date = models.DateTimeField(auto_now_add=True)

