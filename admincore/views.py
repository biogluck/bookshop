from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Count
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from products.models import Book


class AdminView(TemplateView):
    template_name = 'admincore/admin-main.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()  # super(BookCreateView, self)
        book_count = Book.objects.count()
        context['book_count'] = book_count  # 'book'
        book_available = Book.objects.filter(is_available__exact=True).count()
        context['book_available'] = book_available
        book_yesterday = Book.objects.filter(date_created=(
            datetime.now().date() - timedelta(days=31))).count()
        context['book_yesterday'] = book_yesterday
        book_this_month = Book.objects.filter(
            date_created__gte=datetime.today().date().replace(day=1)).count()
        context['book_this_month'] = book_this_month
        genres = Book.objects.all().values('genre__name').annotate(
            dc=Count('genre'))
        context['genres'] = genres
        context['genre_count'] = genres.count()
        return context


class AdminLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            print('staff')
            return ('/admin-shop/')
        else:
            print('nostaff')
            return ('/')


class AdminLogoutView(LogoutView):
    pass
