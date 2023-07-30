from django.db import models

# Create your models here.
class Blog(models.Model):
    user_id = models.IntegerField(null=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    likesUserArray = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.title
    
class UserDatabase(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    userImage = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.username