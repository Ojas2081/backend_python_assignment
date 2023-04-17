import sys
import requests
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from django.contrib.auth.decorators import login_required


def movies(request):
    url = "https://demo.credy.in/api/v1/maya/movies/"
    response = requests.get(url).text
    status_ = status.HTTP_200_OK
    return HttpResponse(response, status=status_)


class CollectionViewSet(viewsets.ModelViewSet):
 
    permission_classes = (IsAuthenticated,)
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        movies = data["movies"]
        movie_ids = []

        collection_ins, _ = Collection.objects.get_or_create(user=request.user,\
                            title=data["title"])
        collection_ins.description = data["description"]
        collection_ins.save()

        for movie in movies:
            movie_ins,_ = Movie.objects.get_or_create(uuid=movie["uuid"])
            movie_ins.title = movie["title"]
            movie_ins.description = movie["description"]
            movie_ins.genre = movie["genre"]
            movie_ins.save()
            movie_ids.append(movie_ins)
        
        collection_ins.movie.clear()
        for movie_id_ in movie_ids:
            collection_ins.movie.add(movie_id_)

        response = [{"collection_uuid": collection_ins.id}]
        return HttpResponse(response, status=status.HTTP_201_CREATED)