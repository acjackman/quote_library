from rest_framework import viewsets

from ..authors.models import Author
from ..quotes.models import Quote

from .permissions import IsAdminOrReadOnly
from .serializers import AuthorSerializer, QuoteSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly, )


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsAdminOrReadOnly, )
