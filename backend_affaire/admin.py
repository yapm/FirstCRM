from django.contrib import admin
from .models import Product, Seller, Bid

admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(Seller)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_produit', 'date_creation')
    list_filter = ('name')
    
