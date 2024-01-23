from django.contrib import admin
from .models import Category,Product,Customer,PurchasedProduct

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(PurchasedProduct)