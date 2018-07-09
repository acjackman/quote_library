from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views import generic

from braces import views as b_views

from .models import Author

AUTHOR_FIELDS = ['prefix', 'first_name', 'middle_name', 'last_name', 'suffix',
                 'birth_date', 'death_date', 'birth_date_year',
                 'death_date_year', 'profession', 'bio', 'notes']


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreateView(b_views.LoginRequiredMixin,
                       b_views.StaffuserRequiredMixin,
                       generic.CreateView):
    model = Author
    fields = AUTHOR_FIELDS


class AuthorUpdateView(b_views.LoginRequiredMixin,
                       b_views.StaffuserRequiredMixin,
                       generic.UpdateView):
    model = Author
    fields = AUTHOR_FIELDS
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse("authors:detail", kwargs={"pk": self.object.pk})


class AuthorDeleteView(b_views.LoginRequiredMixin,
                       b_views.StaffuserRequiredMixin,
                       generic.DeleteView):
    model = Author
    success_url = reverse_lazy('authors:list')
