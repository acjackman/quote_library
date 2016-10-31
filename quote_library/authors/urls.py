from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AuthorListView, name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AuthorDetailView, name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AuthorUpdateView, name='update')
]
