from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='shops/images',default="No Image")


    def __str__(self):
        return self.product_name


class ContactDetails(models.Model):
    customer_id = models.AutoField
    customer_name = models.CharField(max_length=50, default="NO Name")
    customer_email = models.EmailField(max_length=50,default="No email")
    customer_query = models.CharField(max_length=300, default="Query missing")
    query_date = models.DateField()

    def __str__(self):
        return self.customer_email