from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import AuthorRefForm, GenreRefForm, PublisherRefForm, SeriesRefForm
from .models import Author, Genre, Publisher, BookSeries


# Author ref views
class RefAuthorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    # login_url = '/login/'
    template_name = 'reference/ref-list.html'
    model = Author
    permission_required = 'reference.view_author'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()  # super(Author...View, self)
        context['ref_name'] = 'author'
        context['add_url'] = reverse_lazy('reference:author-create')
        return context
    paginate_by = 15


class RefAuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AuthorRefForm  # class!!
    template_name = 'reference/ref_create_update.html'
    success_url = '/admin-shop/ref/author/list/'
    permission_required = 'reference.create_author'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'author'
        return context


class RefAuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AuthorRefForm
    template_name = 'reference/ref_create_update.html'
    model = Author
    success_url = '/admin-shop/ref/author/list/'
    permission_required = 'reference.change_author'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'author'
        return context


class RefAuthorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Author
    template_name = 'reference/ref-detail.html'
    permission_required = 'reference.view_author'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'author'
        return context


class RefAuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = '/admin-shop/ref/author/list/'
    template_name = 'reference/ref_confirm_delete.html'
    permission_required = 'reference.delete_author'


# Genre ref views
#
class RefGenreListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'reference/ref-list.html'
    model = Genre
    paginate_by = 15
    permission_required = 'reference.view_genre'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'genre'
        context['add_url'] = reverse_lazy('reference:genre-create')
        return context


class RefGenreCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = GenreRefForm
    template_name = 'reference/ref_create_update.html'
    success_url = reverse_lazy('reference:genre-list')
    permission_required = 'reference.view_genre'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'genre'
        return context


class RefGenreUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = GenreRefForm
    template_name = 'reference/ref_create_update.html'
    model = Genre
    success_url = reverse_lazy('reference:genre-list')
    permission_required = 'reference.change_genre'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'genre'
        return context


class RefGenreDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Genre
    template_name = 'reference/ref-detail.html'
    permission_required = 'reference.view_genre'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'genre'
        return context


class RefGenreDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Genre
    success_url = '/admin-shop/ref/genre/list/'
    template_name = 'reference/ref_confirm_delete.html'
    permission_required = 'reference.delete_genre'


# Publisher ref views
#
class RefPublisherListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'reference/ref-list.html'
    model = Publisher
    permission_required = 'reference.view_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'publisher'
        context['add_url'] = reverse_lazy('reference:publisher-create')
        return context
    paginate_by = 15


class RefPublisherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PublisherRefForm
    template_name = 'reference/ref_create_update.html'
    success_url = reverse_lazy('reference:publisher-list')
    permission_required = 'reference.view_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'publisher'
        return context


class RefPublisherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PublisherRefForm
    template_name = 'reference/ref_create_update.html'
    model = Publisher
    success_url = reverse_lazy('reference:publisher-list')
    permission_required = 'reference.change_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'publisher'
        return context


class RefPublisherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Publisher
    template_name = 'reference/ref-detail.html'
    permission_required = 'reference.view_publisher'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'publisher'
        return context


class RefPublisherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Publisher
    success_url = reverse_lazy('reference:publisher-list')
    template_name = 'reference/ref_confirm_delete.html'
    permission_required = 'reference.delete_publisher'


# Series ref views
#
class RefSeriesListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'reference/ref-list.html'
    model = BookSeries
    paginate_by = 15
    permission_required = 'reference.view_series'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'series'
        context['add_url'] = reverse_lazy('reference:series-create')
        return context


class RefSeriesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SeriesRefForm
    template_name = 'reference/ref_create_update.html'
    success_url = reverse_lazy('reference:series-list')
    permission_required = 'reference.create_series'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'series'
        return context


class RefSeriesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SeriesRefForm
    template_name = 'reference/ref_create_update.html'
    model = BookSeries
    success_url = reverse_lazy('reference:series-list')
    permission_required = 'reference.change_series'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'series'
        return context


class RefSeriesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = BookSeries
    template_name = 'reference/ref-detail.html'
    permission_required = 'reference.view_series'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ref_name'] = 'series'
        return context


class RefSeriesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BookSeries
    success_url = reverse_lazy('reference:series-list')
    template_name = 'reference/ref_confirm_delete.html'
    permission_required = 'reference.delete_series'
