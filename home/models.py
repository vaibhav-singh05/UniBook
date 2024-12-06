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