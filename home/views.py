from django.shortcuts import render,redirect
from .models import Product,Slider
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    products=Product.objects.all()
    slides=Slider.objects.all()
    context={
        'products':products,
        'slides':slides
    }
    return render(request,'index.html',context)

def login_user(request):
    if request.method == "POST": 
        username =request.POST['username']
        password =request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            messages.success(request,("login succesfll"))
            return redirect('home')
        else:
            messages.success(request,("invalid credentials"))
            return redirect ('login')    
    else:
        return render (request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("logout succesfull"))    
    return redirect('home')


