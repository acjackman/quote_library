from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AuthorListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='detail'),
    url(r'^create/$', views.AuthorCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AuthorUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AuthorDeleteView.as_view(), name='delete'),
]
