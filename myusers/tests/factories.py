"""Factories for our custom user application."""

# factories.py
import factory
from . import models


class CustomUserFactory(factory.django.DjangoModelFactory):
    """A factory for our custom user object.

    By default all objects will have the user name homer.simpson.000
    where 000 will increment sequentially as more users are added.

    The password for all users will be "password123".

    """

    class Meta:
        model = models.CustomUser

    username_name = factory.Sequence(lambda n: "simpson.homer.%03d" % n)
    email = factory.Sequence(lambda n: "homer.%03d@simpsons.com" % n)
    password = "password123"
