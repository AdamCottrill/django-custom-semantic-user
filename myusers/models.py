"""Model for our custome user class"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    """A custom user based on django's AbstractUser."""

    def __str__(self):
        """the User's e-mail will be the string representation.

        Arguments:
        - `self`:
        """
        return self.email
