from django.contrib import admin
from .models import Category, Supplier, Product, StockTransaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'phone_number')
    search_fields = ('name', 'contact_email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'price', 'stock_quantity', 'last_updated')
    list_filter = ('category', 'supplier')
    search_fields = ('name',)
    list_editable = ('price', 'stock_quantity')

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'transaction_type', 'quantity', 'date')
    list_filter = ('transaction_type', 'date')
    search_fields = ('product__name',)