from django.contrib import admin
from .models import Size, Color, GeneralCategory, Category, Campaign, Products, ProductImages
from customer.models import Review


# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    readonly_fields = ['image_tag']
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review
    readonly_fields = ['customer', 'star_count', 'comment']
    extra = 0

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline, ReviewInline]
    readonly_fields = ['slug']


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(ProductImages)
