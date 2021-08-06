from django import template
from cart.models import Product

register = template.Library()

@register.inclusion_tag('cart/product/latest_product.html')
def show_latest_products():
    latest_products = Product.objects.all().order_by('id')[:4]
    return {'latest_products': latest_products}