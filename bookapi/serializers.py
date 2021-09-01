from rest_framework import serializers
from .models import Book, db


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.ListField(child=serializers.CharField())
    categories = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Book
        fields = ('id','title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count', 'thumbnail')

class dbSerializer(serializers.ModelSerializer):
    class Meta:
        model = db
        fields = ('id',)
