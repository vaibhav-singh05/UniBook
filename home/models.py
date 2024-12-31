from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', default='profile_pics/default.jpg')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
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
        return self.title
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"