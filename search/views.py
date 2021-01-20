from django.views.generic import TemplateView, FormView
from django.db.models import Q

from products.models import Book


class SearchView(TemplateView):
    template_name = "search/search.html"


class MakeSearchView(TemplateView):
    template_name = "search/search-results.html"

    # try to define form for validation
    def get_context_data(self, **kwargs):
        context = super(MakeSearchView, self).get_context_data(**kwargs)
        name = self.request.GET.get('name')
        author = self.request.GET.get('author')
        year = self.request.GET.get('year')
        results = None
        if name:
            results = Book.objects.filter(
                name__icontains=name
            )
        if author:
            if not results:
                results = Book.objects.filter(author__name__icontains=author)
            else:
                results = results.filter(author__name__icontains=author)

        if year:
            if not results:
                results = Book.objects.filter(year__icontains=year)
            else:
                results = results.filter(year__icontains=year)

        # print(results)
        context['query_results'] = results
        return context
