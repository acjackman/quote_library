from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.QuoteListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.QuoteDetailView.as_view(), name='detail'),
    url(r'^create/$', views.QuoteCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.QuoteUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.QuoteDeleteView.as_view(), name='delete'),
]
