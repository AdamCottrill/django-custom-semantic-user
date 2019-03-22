"""Fixtures for our custom user app."""

import pytest
# from .factories import CustomUserFactory
from myusers.models import CustomUser

@pytest.fixture(scope='function')
def joe_user(db):
    """return a normal user named joe user """
    password = "Abcd1234"
    joe = CustomUser(
        username='joeuser',
        first_name='Joe',
        last_name='User',
        email='joeuser@gmail.com',
        password=password)
    joe.save()
    return joe
