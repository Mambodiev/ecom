from django.contrib import admin
from .models import Customer, Carousel, Terms_of_use, Faq, About, Shipping_returns, Privacy_policy


class AboutAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'About', {'fields': ('about_text_en', 'about_text_fr','name',)})
        ]


class FaqAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'Faq', {'fields': ('faq_text_en', 'faq_text_fr', 'name',)})
        ]


class Privacy_policyAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'Privacy_policy', {'fields': ('privacy_policy_text_en', 'privacy_policy_text_fr','name',)})
        ]


class Shipping_returnsAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'Shipping_returns', {'fields': ('shipping_returns_text_en', 'shipping_returns_text_fr','name',)})
        ]

class Terms_of_useAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'Terms_of_use', {'fields': ('terms_of_use_text_en', 'terms_of_use_text_fr','name',)})
        ]




admin.site.register(Customer)
admin.site.register(Carousel)
admin.site.register(About, AboutAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Terms_of_use, Terms_of_useAdmin)
admin.site.register(Shipping_returns, Shipping_returnsAdmin)
admin.site.register(Privacy_policy, Privacy_policyAdmin)
