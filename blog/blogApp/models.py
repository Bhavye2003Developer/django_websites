from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.author} -> {self.title}'