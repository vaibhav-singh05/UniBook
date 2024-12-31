from django.contrib import admin
from home.models import Contact
from home.models import Product
from home.models import Profile

# Register your models here.

admin.site.register(Profile)

admin.site.register(Contact)

admin.site.register(Product)
