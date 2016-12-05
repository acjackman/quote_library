from rest_framework import serializers

from ..authors.models import Author
from ..quotes.models import Quote


class AuthorSerializer(serializers.ModelSerializer):
    # quotes = serializers.HyperlinkedRelatedField(many=True, view_name='quote-detail', read_only=True)

    class Meta:
        model = Author
        fields = (
            # 'quotes',
            'id',
            'prefix',
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'birth_date',
            'death_date',
            'birth_date_year',
            'death_date_year',
            'profession',
            'bio',
            'notes',
        )


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'id',
            'text',
            'author',
            'added',
            'date',
            'source',
            'reference',
            'verified',
            'rating',
        )
