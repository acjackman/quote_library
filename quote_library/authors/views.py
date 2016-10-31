from django.views.generic import ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse

from .models import Author


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class AuthorUpdateView(UpdateView):
    model = Author

    def get_success_url(self):
        return reverse("authors:detail", kwargs={"pk": self.object.pk})
