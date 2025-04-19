from django.shortcuts import render,redirect
from .models import Product,Slider,Category
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.shortcuts import get_object_or_404

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


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log in the user directly
            messages.success(request, ("Account created successfully!"))
            return redirect('home')
        else:
            messages.error(request, ("There was a problem with your registration. Please try again."))
    return render(request, 'register.html', {'form': form})

def product(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'product.html', {'product': product})

def mobiles(request, cat):
    cat = cat.replace('-', ' ')

    try:
        category = Category.objects.get(name__iexact=cat)
        products = Product.objects.filter(categories=category)
        return render(request, 'mobiles.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.error(request, "Category not found")
        return redirect('home')

    