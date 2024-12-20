from django.shortcuts import render
from .models import Category, Product, StockTransaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all()
    return render(request, 'UI/home.html', {'categories': categories})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'UI/product_list.html', {'products': products})

def stock_transactions(request):
    transactions = StockTransaction.objects.all()
    return render(request, 'UI/stock_transactions.html', {'transactions': transactions})

@login_required
def home_view(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home.html
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'UI/register.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'UI/register.html')
        
        # Create the user
        user = User.objects.create_user(username=username, password=password, first_name=name)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')  # Redirect to login page
    
    return render(request, 'register.html')

# Home view
@login_required
def home_view(request):
    return render(request, 'home.html')

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')