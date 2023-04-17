import sys
import requests
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from django.conf import settings
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site


class UserViewSet(viewsets.ModelViewSet):
 
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], url_path='register',
        permission_classes=(AllowAny,))
    def register(self, request):
        try:
            data = request.data

            username = data.get('username', None)
            password = data.get('password', None)

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None

            if user:
                response = [{
                    "message": "A user with this email already exists."
                    }]
                status_ = status.HTTP_400_BAD_REQUEST
            else:
                user = User.objects.create(**data)
                user.set_password(password)
                user.is_active = True
                user.save()

                ################## TOKEN OBTAIN PAIR #######################

                site = get_current_site(request)
                url = "http://{}/token/".format(site)
                data ={'username':username, "password":password}
                response = requests.post(url, data=data)

                ################## TOKEN OBTAIN PAIR #######################
                response = [{
                    'username': username,
                    'access_token': response.json()['access']
                    }]
                status_ = status.HTTP_201_CREATED
        except Exception as error:
            response = {}
            print("Register line number of error is {}".format(sys.exc_info()[-1].tb_lineno), error)
        return HttpResponse(response, status=status_)