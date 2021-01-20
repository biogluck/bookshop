from django.shortcuts import render

from django.views.generic import (
    UpdateView, DetailView, ListView, DeleteView, CreateView)

from django.urls import reverse_lazy

from .forms import CheckoutOrderForm
from .models import Order, OrderStatus


class OrderCheckoutView(CreateView):
    model = Order
    template_name = 'cart/view-list.html'
    form_class = CheckoutOrderForm

    def get_success_url(self):
        del self.request.session['cart_id']
        return reverse_lazy('orders:success', kwargs={'pk': self.object.pk})


class OrderCheckoutSuccess(DetailView):
    model = Order
    template_name = 'orders/success.html'


class OrdersListAdmin(ListView):
    model = Order
    template_name = 'orders/list-admin.html'
    paginate_by = 10


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order-detail.html'

    '''
    change status to "Processing"
    '''
    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        obj.status = OrderStatus.objects.get(pk=2)
        obj.save()
        return obj
