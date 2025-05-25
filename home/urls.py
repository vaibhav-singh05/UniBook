from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.loginUser, name= 'login'),
    path('logout', views.logoutUser, name= 'logout'),
    path('register', views.register, name= 'register'),
    path('sell', views.sell, name= 'sell'),
    # path('products/success/', views.product_success, name='some_success_url'), #Define the success url
    path('my_profile', views.my_profile, name='my_profile'),
    path('edit_profile', views.update_profile, name='update_profile'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart', views.cart, name='cart'),
    path('carts', views.carts, name='carts'),
    path('checkout/', views.checkout, name='checkout'),
]