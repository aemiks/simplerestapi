from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import filters
from .models import Book
from django.db.models.query import Q
from bookapi.serializers import BookSerializer
import requests

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        ## filtering and sorting based on get_queryset ##

        ## filtering by ?published_date= ##
        published_date = self.request.query_params.get('published_date', None)
        ## sorting by ?sort=
        sort = self.request.query_params.get('sort', None)
        if sort:
            if published_date:
                books = Book.objects.filter(published_date__contains=published_date).order_by(sort)
            else:
               books = Book.objects.all().order_by(sort)
        else:
            if published_date:
                books = Book.objects.filter(published_date__contains=published_date)
            else:
                books = Book.objects.all()

        author = self.request.query_params.get('author', None) ## filtering by ?author=
        if author:
            books = Book.objects.filter(authors=[author])

        return books

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    #def retrieve(self, request, *args, **kwargs):
    #    instance = self.get_object()
    #    serializer = self.get_serializer(instance)
    #    return Response(serializer.data)

    def get_data(request):
        ## getting the json from the url and format to get the object ##
        url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
        req = requests.get(url)
        data = req.json()

        ## list of json_id in our database - to not multiply objects ##
        json_id_list = []
        for book in Book.objects.all():
            json_id_list.append(book.json_id)

        for i in range(0,len(data['items'])): ## loop through all objects'items' in json ##
            book_dict = data['items'][i]
            json_id = book_dict['id']
            book_dict = book_dict['volumeInfo']

            ## fetching values to the model ##
            title = book_dict['title']
            authors = book_dict['authors']
            published_date = book_dict['publishedDate']
            categories = book_dict['categories']
            if 'averageRating' in book_dict is not None:
                average_rating = book_dict['averageRating']
            else:
                average_rating = 0
            if 'ratingsCount' in book_dict is not None:
                ratings_count = book_dict['ratingsCount']
            else:
                ratings_count = 0
            if 'imageLinks' in book_dict is not None:
                thumbnail = book_dict['imageLinks']['thumbnail']
            else:
                thumbnail = 'brak'

            ## check if an object is not in the database, if not create new##
            if json_id in json_id_list:
                continue
            else:
                book = Book.objects.create(title=title or None, authors=authors or None, published_date=published_date or None,
                                                categories=categories or None, average_rating=average_rating or None,
                                                ratings_count=ratings_count or None, thumbnail=thumbnail or None, json_id=json_id)
                book.save()

        books_list = Book.objects.all()

        ## loop to format text into date(year) ##
        #for book in books_list:
        #    year = book.published_date_format()
        #    year = int(year)
        #    book.published_year = year
        #    book.save()

        return render(request, 'books.html', {'books_list': books_list})


