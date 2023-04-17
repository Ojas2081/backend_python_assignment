from django.urls import re_path as url
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'collection', views.CollectionViewSet, basename='collection')

urlpatterns = [
        url('movies', views.movies, name='movies'),
    ]

urlpatterns += router.urls 