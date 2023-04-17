from django.db import models
import uuid
# Create your models here.


class Movie(models.Model):
    uuid = models.CharField(primary_key=True, max_length=200, unique=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.title)


class Collection(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ManyToManyField('Movie', null=True, blank=True)

    def __str__(self):
        return "%s-%s" % (self.user, self.title)