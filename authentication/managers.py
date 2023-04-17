from django.contrib.auth.models import (
    BaseUserManager
)
from django.db import models


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, first_name, last_name, email, password=None, username=None):
        """Create and return a `User` with an email, username and password."""
        if first_name is None or last_name is None:
            raise TypeError('Users must have first_name and last_name.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(first_name=first_name,
                          last_name=last_name,
                          email=self.normalize_email(email),
                          username=username)
        user.set_password(password)
        user.email_verified = False
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password, username=None):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(first_name, last_name, email, password, username)
        user.is_superuser = True
        user.is_staff = True
        user.email_verified = True
        user.save()

        return user
