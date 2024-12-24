from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.firstname
    
class Product(models.Model):
    product_id = models.AutoField
    product_category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    image1 = models.ImageField(upload_to="images/")
    image2 = models.ImageField(upload_to="images/")
    image3 = models.ImageField(upload_to="images/")
    mobile = models.CharField(max_length=12, default="")
    location = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.product_category
    