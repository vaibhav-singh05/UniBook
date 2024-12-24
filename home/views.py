from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login, get_user_model

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


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

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.mobile=mobile
        user.save()
        messages.success(request, "Your have registered successfully")

    return render(request, 'register.html')

def sell(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'sell.html')