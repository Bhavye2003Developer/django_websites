from django.db import models

# Create your models here.
class BusinessMan(models.Model):
    userID = models.IntegerField()
    username = models.CharField(max_length=100)
    userImage = models.ImageField(default="No image",upload_to='gallery')
    profession = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    phoneNumber = models.CharField(max_length=50, help_text="Enter phone number with country code", default="+919999999999")
    worksByUser = models.TextField(max_length=1000, default="Enter a list of works by user")
    galleryImages1 = models.ImageField(default="No image",upload_to='gallery')
    galleryImages2 = models.ImageField(default="No image",upload_to='gallery')
    galleryImages3 = models.ImageField(default="No image",upload_to='gallery')
    galleryImages4 = models.ImageField(default="No image",upload_to='gallery')
    galleryImages5 = models.ImageField(default="No image",upload_to='gallery')

    def __str__(self) -> str:
        return self.username