from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.ListField(child=serializers.CharField())
    categories = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Book
        fields = ('id','title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count', 'thumbnail')