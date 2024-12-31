from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from home.models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login, get_user_model
from .models import Product
from .models import Profile
from django.shortcuts import render, get_object_or_404
from.models import Product, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    products = Product.objects.all()
    params = {'product': products}
    return render(request, 'index.html', params)


def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'about.html')


def contact(request):
        if request.user.is_anonymous:
            return redirect('/login')
        
        if request.method == 'POST':
             firstname = request.POST.get('firstname')
             lastname = request.POST.get('lastname')
             mobile = request.POST.get('mobile')
             email = request.POST.get('email')
             state = request.POST.get('state')
             contact = Contact(firstname=firstname, lastname=lastname, mobile=mobile, email=email, state=state, date=datetime.today())
             contact.save()
             messages.success(request, "Your details has been sent!")
             
        return render(request, 'contact.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credetials
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
            
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.method =='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        check_user = User.objects.filter(email = email).first()
        check_profile = Profile.objects.filter(mobile = mobile).first()

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists")
            return redirect('register')
        
        if Profile.objects.filter(mobile=mobile).exists():
            messages.warning(request, "Mobile number already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()

        profile = Profile(user=user, mobile=mobile)
        profile.save()

        messages.success(request, "Your have registered successfully")

    return render(request, 'register.html')


def sell(request):
        if request.user.is_anonymous:
            return redirect('/login')
        
        if request.method == 'POST':
             product_category = request.POST.get('product_category')
             title = request.POST.get('title')
             desc = request.POST.get('desc')
             price = request.POST.get('price')
             image1 = request.FILES.get('image1')
             image2 = request.FILES.get('image2')
             image3 = request.FILES.get('image3')
             mobile = request.POST.get('mobile')
             location = request.POST.get('location')
             sell = Product(product_category=product_category, title=title, desc=desc, price=price, image1=image1,image2=image2, image3=image3, mobile=mobile, location=location, user=request.user, date=datetime.now())
             sell.save()
             messages.success(request, "Succesfully Posted!")
        return render(request, 'sell.html')


#def product_success(request):
    #return render(request, 'product_success.html') #Create a success template       

@login_required
def my_profile(request):
    # Get the logged-in user's profile
    user = request.user
    try:
        # Fetch the user's profile
        user_profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        user_profile = None  # In case the profile doesn't exist yet

    # Fetch the products uploaded by the user
    user_products = Product.objects.filter(mobile=user.profile.mobile)

    # Pass the user details, profile, and products to the template
    context = {
        'user': user,
        'user_profile': user_profile,
        'user_products': user_products,  # Send the list of products
    }
    return render(request, 'my_profile.html', context)

@login_required
def update_profile(request):
    # Get the logged-in user's profile
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, "Profile does not exist.")
        return redirect('my_profile')

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')  # Correct field name for the profile picture
        bio = request.POST.get('bio')  # Get the bio text (optional)
        
        if profile_pic:
            user_profile.profile_pic = profile_pic  # Update profile picture if uploaded
        if bio:
            user_profile.bio = bio  # Update bio if provided
        
        user_profile.save()  # Save the profile updates
        messages.success(request, "Profile updated successfully!")
        return redirect('my_profile')  # Redirect to the user's profile page
    
    return render(request, 'update_profile.html', {'user_profile': user_profile})

def product_detail(request, product_id):
    # Fetch the product using the product_id or return a 404 if not found
    product = get_object_or_404(Product, id=product_id)
    
    # Render the product detail page, passing the product data to the template
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    # Add product to cart
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.title} added to cart.")
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    # Remove item from cart
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart')

@login_required
def cart(request):
    # Fetch the user's cart items
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

