from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    title = models.CharField(max_length=250)
    authors = ArrayField(ArrayField(models.CharField(max_length=100)))
    published_date = models.TextField(max_length=50)
    categories = ArrayField(ArrayField(models.CharField(max_length=100)))
    average_rating = models.FloatField(blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField()
    json_id = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.title

class db(models.Model):
    key = models.CharField(max_length=1)


