from django import template

from tree_menu.models import Product

register = template.Library()


@register.inclusion_tag('tree_menu/templatetags/menu.html')
def draw_menu():
    products = Product.objects.all()
    return {'products': products}
