from inventory import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),
    path('transactions/', views.stock_transactions, name='stock_transactions'),
    path('', include('inventory.urls')),
]
