from django.contrib import admin
from .models import Coupon, Order, OrderProduct

# Register your models here.

admin.site.register(Coupon)

class OrderedProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ['title', 'count', 'price', 'size', 'color']
    extra = 0


@admin.register(Order)  
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderedProductInline]