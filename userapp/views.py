from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    DetailView,
)

from products.models import Book


class UserHomeView(TemplateView):
    template_name = 'userapp/user-home.html'

    # testing sessions behavior
    def get(self, request, *args, **kwargs):
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits+1
        context = self.get_context_data(**kwargs)
        # request.session.clear()
        return self.render_to_response(context)


class UserBookDetailView(DetailView):
    model = Book
    template_name = "userapp/user-book.html"


class UserBookList(ListView):
    model = Book
    context_object_name = 'object_list'
    template_name = 'userapp/book-list.html'
    paginate_by = 6


class AboutView(TemplateView):
    template_name = 'userapp/about.html'


class DeliveryView(TemplateView):
    template_name = 'userapp/delivery.html'
