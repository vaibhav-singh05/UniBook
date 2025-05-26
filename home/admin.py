from django.contrib import admin
from home.models import Contact
from home.models import Product
from home.models import Profile
from .models import Order
from .models import OrderItem

# Register your models here.

admin.site.register(Profile)

admin.site.register(Contact)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(OrderItem)