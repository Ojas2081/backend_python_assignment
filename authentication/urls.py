from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
]

urlpatterns += router.urls 