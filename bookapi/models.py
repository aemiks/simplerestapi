from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime as dt

# Create your models here.

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

    ## Text field format to get year ##
    #def published_date_format(self):
    #    if len(self.published_date) > 5:
    #        converted_date = dt.strptime(self.published_date, "%Y-%m-%d")
    #        self.published_year = converted_date.year
    #    else:
    #        converted_date = dt.strptime(self.published_date, "%Y")
    #        self.published_year = converted_date.year
    #    return self.published_year