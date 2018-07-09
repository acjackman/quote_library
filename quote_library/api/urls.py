from __future__ import unicode_literals

from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

# Use a router to route the viewsets
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'quotes', views.QuoteViewSet)

# Schema generated automatically using CoreAPI
schema_view = get_schema_view(title='Quote Library API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]
