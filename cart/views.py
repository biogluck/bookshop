from django.shortcuts import render
from django.views.generic import (
    UpdateView,
    ListView,
    DeleteView,
    DetailView,
    RedirectView,
)
from django.urls import reverse_lazy
from .models import Cart, ProductsInCart
from orders.models import Order, OrderStatus
from .forms import AddToCartForm
from products.models import Book
from orders.forms import CheckoutOrderForm


class CartListView(DetailView):  # DetailView
    template_name = 'cart/cart-list.html'
    model = ProductsInCart

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_form = CheckoutOrderForm()
        checkout_form.fields['cart'].initial = self.object
        checkout_form.fields['status'].initial = OrderStatus.objects.get(pk=1)
        context["form"] = checkout_form
        return context

    def get_object(self):
        cart_id = self.request.session.get('cart_id')
        default_user = self.request.user if self.request.user.is_authenticated else None
        cart, cart_created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'user': default_user,
            }
        )
        return cart


class AddToCartView(UpdateView):
    template_name = "cart/add-to-cart.html"
    form_class = AddToCartForm
    model = ProductsInCart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('S: ', dir(self.request.session))
        return context

    def get_object(self):
        cart_id = self.request.session.get('cart_id')
        default_user = self.request.user if self.request.user.is_authenticated else None
        print('user:', default_user)
        cart, cart_created = Cart.objects.get_or_create(
            pk=cart_id,
            user=default_user,
            defaults={
                'user': default_user,
            },
        )
        # 'product' прилетает из запроса
        book_id = self.kwargs.get('product')
        book = Book.objects.get(pk=book_id)
        obj, obj_created = ProductsInCart.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={
                'cart': cart,
                'book': book,
                'quantity': 1,
            }
        )
        if obj_created:
            self.request.session['cart_id'] = cart.pk
        elif not obj_created:
            obj.quantity += 1
        return obj


class CartItemDeleteView(DeleteView):
    model = ProductsInCart
    template_name = 'cart/delete-item.html'


class ClearCartView(RedirectView):
    url = '/book-list/'

    def dispatch(self, request, *args, **kwargs):
        ProductsInCart.objects.all().delete()
        return super(ClearCartView, self).dispatch(request, *args, **kwargs)
