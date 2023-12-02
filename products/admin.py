from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    ''' Class to modify the categories in the admin panel '''

    # Category fields to display in the admin panel
    list_display = (
        'friendly_name',
        'name'
    )


class ProductAdmin(admin.ModelAdmin):
    ''' Class to modify the products in the admin panel '''
    
    # Product fields to display in the admin panel
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )
        
    # Sorting the products in the admin panel by SKU
    ordering = ('sku',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
