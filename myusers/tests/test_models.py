"""Unit tests to verify that methods associated with our models are
working as they should."""

from ..models import CustomUser


def test_custom_user_str():
    """the str method of our custom user should return the user's email.

    Arguments:
    - `self`:
    """

    email = 'homer@simpson.com'
    homer = CustomUser(
        username="homer.simpson", password="password123", email=email)

    assert str(homer) == email
