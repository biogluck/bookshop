from decimal import Decimal
from django.conf import settings
from products.models import Book


class Cart(object):
    """     
    Чэсна стырыў рэалізацыю з інтэрнэта
    """

    def __init__(self, request):
        """ 
        initialize
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart   # make attr cart (dict)

    def add(self, product, quantity=1, update_quantity=False):
        """
        add book and/or set quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            # add dict with quant and price
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)}
        if update_quantity:
            # update Q
            self.cart[product_id]['quantity'] = quantity
        else:
            # increment Q
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        remove product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over items and update data
        """
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = str(product.name)

        for item in self.cart.values():
            item['total_price'] = Decimal(item['price']) * item['quantity']
            item['price'] = item['price']  # Decimal
            yield item

    def __len__(self):
        """
        Count books in Cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Total price
        """
        return sum(float(item['price'])*int(item['quantity']) for item in self.cart.values())
        # Decimal(int(item['price'])) * item['quantity']

    def clear(self):
        # delete Cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
