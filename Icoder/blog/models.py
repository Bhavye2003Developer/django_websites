from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    postComment = models.TextField()
    timestamp = models.DateField(auto_now_add=True, blank=True)
    updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.name