from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views import generic

from braces import views as b_views

from .models import Quote

QUOTE_FIELDS = ['text', 'date', 'source', 'reference', 'verified', 'rating', 'added']


class QuoteListView(generic.ListView):
    model = Quote


class QuoteDetailView(generic.DetailView):
    model = Quote


class QuoteCreateView(b_views.LoginRequiredMixin,
                      b_views.StaffuserRequiredMixin,
                      generic.CreateView):
    model = Quote
    fields = QUOTE_FIELDS


class QuoteUpdateView(b_views.LoginRequiredMixin,
                      b_views.StaffuserRequiredMixin,
                      generic.UpdateView):
    model = Quote
    fields = QUOTE_FIELDS
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse("quotes:detail", kwargs={"pk": self.object.pk})


class QuoteDeleteView(b_views.LoginRequiredMixin,
                      b_views.StaffuserRequiredMixin,
                      generic.DeleteView):
    model = Quote
    success_url = reverse_lazy('quotes:list')
