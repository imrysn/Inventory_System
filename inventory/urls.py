from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),  
    path('transactions/', views.stock_transactions, name='stock_transactions'),  
    path('products/transactions/', views.stock_transactions, name='stock_transactions'),
    path('transactions/products/', views.product_list, name='products_list'),
]
