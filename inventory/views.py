from django.shortcuts import render, redirect
from .models import Category, Product, Supplier, StockTransaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
import json


# Home View
@login_required
def home(request):
    categories = Category.objects.all()

    # Calculate totals for dashboard
    total_products = Product.objects.count()
    total_suppliers = Supplier.objects.count()
    out_of_stock = Product.objects.filter(stock_quantity=0).count()
    low_stock = Product.objects.filter(stock_quantity__lte=F('reorder_level')).count()

    # For category stock data (used in the chart)
    stock_quantities = Product.objects.values('category__name').annotate(total_stock=Sum('stock_quantity'))
    category_labels = [category['category__name'] for category in stock_quantities]
    category_data = [category['total_stock'] for category in stock_quantities]

    # For top products (used in the chart)
    top_products = Product.objects.order_by('-stock_quantity')[:5]
    top_product_names = [product.name for product in top_products]
    top_product_sales = [product.stock_quantity for product in top_products]

    context = {
        'categories': categories,
        'total_products': total_products,
        'total_suppliers': total_suppliers,
        'out_of_stock': out_of_stock,
        'low_stock': low_stock,
        'stock_quantities': stock_quantities,
        'category_labels': json.dumps(category_labels), 
        'category_data': json.dumps(category_data),      
        'top_product_names': json.dumps(top_product_names), 
        'top_product_sales': json.dumps(top_product_sales),  
    }

    return render(request, 'UI/home.html', context)




# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'register.html')
        
        # Create the user
        user = User.objects.create_user(username=username, password=password, first_name=name)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')  # Redirect to login page
    
    return render(request, 'register.html')


# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
