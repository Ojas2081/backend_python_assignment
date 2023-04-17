from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    first_name = models.CharField(db_index=True, max_length=15, null=True)
    last_name = models.CharField(db_index=True, max_length=15, null=True)
    username = models.CharField(db_index=True, unique=True, max_length=15, null=True)
    email = models.EmailField(db_index=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.username