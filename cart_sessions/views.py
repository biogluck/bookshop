from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import AddToCartSessionForm
from products.models import Book
from .cart import Cart


class CartSessionListView(TemplateView):
    template_name = 'cart_sessions/cart-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        cart = Cart(self.request)
        context['book_list'] = self.request.session.get('cart')
        for x in cart:
            print(type(x), x)
        context['book_quantity'] = len(cart)
        context['total_price'] = str(cart.get_total_price())
        return context


class AddToCartSessionView(FormView):
    template_name = "cart_sessions/add-to-cart-session.html"
    form_class = AddToCartSessionForm
    success_url = reverse_lazy('cart_sess:cart-list')

#    def get(self, request, *args, **kwargs):
#        """Handle GET requests: instantiate a blank version of the form."""
#        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        book_id = self.kwargs.get('product')
        book = Book.objects.get(pk=book_id)
        form = AddToCartSessionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=book,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
            print(self.request.session)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ClearCartSessionView(RedirectView):
    url = reverse_lazy('cart_sess:cart-list')

    def dispatch(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return super(ClearCartSessionView, self).dispatch(request, *args, **kwargs)
