from datetime import datetime, timedelta

from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic import View, TemplateView

from django.db.models import Count

from django.http.response import HttpResponse
from django.urls import reverse_lazy
# Create your views here.

from .models import Book
from .forms import BookForm


class BookListView(ListView):
    template_name = 'products/book-list.html'
    model = Book
    paginate_by = 13

    def get_context_data(self, *args, **kwargs):  # +
        context = super().get_context_data()  # super(AuthorRefCreateView, self)
        context['view_name'] = 'book'
        context['add_url'] = reverse_lazy('reference:author-create')
        return context
    

class BookCreateView(CreateView):
    template_name = 'book_create_update.html'
    form_class = BookForm
    success_url = reverse_lazy('products:book-list')


class BookUpdateView(UpdateView):
    form_class = BookForm
    template_name = 'book_create_update.html'
    model = Book
    success_url = reverse_lazy('products:book-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['view_name'] = 'book'
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()  # super(BookCreateView, self)
        context['view_name'] = 'book'
        return context


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('products:book-list')
    template_name = 'book_confirm_delete.html'
