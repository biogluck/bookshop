from django import template
from cart.models import Cart

register = template.Library()


@register.inclusion_tag('admincore/cart/icon-top.html', takes_context=True)
def top_cart_icon(context):
    """
    получить число товаров в корзине
    """
    cart_id = context['request'].session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(pk=int(cart_id))
        products = cart.products_in_cart.all().count()  # products - link in model
    else:
        products = 0
    return {
        'products': products,
    }
