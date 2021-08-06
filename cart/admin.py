from django.contrib import admin
from .models import (
    Product, OrderItem, Order, ColourVariation,
    SizeVariation, Address, Payment, Comment, Category, StripePayment, Image, Product_detail
)


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'user', 'product', 'rate', 'id')


class ProductAdmin(admin.ModelAdmin):
    list_display = [
                    'title', 
                    'active',
                    'price', 
                    'stock', 
                    'updated']
    # list_filter = ['status']
    fieldsets = [
            (u'ColourVariation', {'fields': (
                    'title_en',
                    'slug_en',
                    'featured',
                    'available_colours',
                    'available_sizes',
                    'active',
                    'primary_category',
                    'secondary_categories',
                    'price', 
                    'stock', 
                    'title_fr',
                    'slug_fr',
                    
                    
            )})
        ]
    prepopulated_fields = {'slug_en': ('title_en',), 'slug_fr': ('title_fr',)}


class SizeVariationAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'SizeVariation', {'fields': ('name_en', 'name_fr',)})
        ]
        

class ColourVariationAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'ColourVariation', {'fields': ('name_en', 'name_fr',)})
        ]


class Product_detailAdmin(admin.ModelAdmin):
    list_display = ['title',]


admin.site.register(Category)
admin.site.register(Address, AddressAdmin)
admin.site.register(ColourVariation,ColourVariationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SizeVariation, SizeVariationAdmin)
admin.site.register(Payment)
admin.site.register(StripePayment)
admin.site.register(Image)
admin.site.register(Product_detail, Product_detailAdmin)