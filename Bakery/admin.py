from django.contrib import admin
from . models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fulltname', 'othername', 'gender', 'quarter', 'address', 'tel', 'tel2', 'created', 'updated')

# Register your models here.
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('fulltname', 'othername', 'gender', 'quarter', 'address', 'tel', 'tel2', 'created', 'updated')

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cost_price', 'selling_price','created', 'updated')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Catergory)
