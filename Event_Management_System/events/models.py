from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    event_date = models.DateTimeField('event date')
    event_location = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images/', null=True, blank=True, default=None)
    event_is_featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.event_title