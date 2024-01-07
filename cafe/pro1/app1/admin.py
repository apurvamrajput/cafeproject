from django.contrib import admin
from .models import User,Customer,Product,Order,Order_item,ShippingAddress

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["Username","fname","lname","email"]
# admin.site.register(User,UserAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user","name","email"]
admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","digital"]
admin.site.register(Product,ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer","date_ordered","complete","transaction_id"]
admin.site.register(Order,OrderAdmin)


class Order_itemAdmin(admin.ModelAdmin):
    list_display = ["product","order","quantity","date_added"]
admin.site.register(Order_item,Order_itemAdmin)
