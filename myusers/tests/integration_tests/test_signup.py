"""Integration tests for signup template

The signup view extends uses a custom template. The tests in this file
verify that the custom templates contains all of the necessary
elements including error messages and mark-up.

Tests in this file include:

+ form elements
+ form success
+ missing username
+ missing email
+ missing password1
+ missing password2
+ passwords do not match
+ passwords too short
+ username exists
+ email exists


"""
import pytest

from django.urls import reverse


def test_form_elements(client):
    """verify that the signup form contains the expected elements."""

    response = client.get(reverse('signup'))
    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')

    assert "Sign-Up" in content
    assert "Username:" in content
    assert "Email address:" in content
    assert "Password:" in content
    assert "Password confirmation:" in content


@pytest.mark.django_db
def test_form_success(client):
    """Verify that we can sign up a new user with our form."""

    data = {
        'username': 'bartsimpson',
        'email': 'bart@simpsons.com',
        'password1': 'Django123',
        'password2': 'Django123',
    }

    response = client.post(reverse('signup'), data=data, follow=True)
    assert 'registration/login.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')


@pytest.mark.django_db
def test_form_missing_username(client):
    """If we submit the form without a username, we should see an
bmo    appropriate error messages."""

    data = {
        'email': 'bart@simpsons.com',
        'password1': 'Django123',
        'password2': 'Django123',
    }

    response = client.post(reverse('signup'), data=data, follow=True)
    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')

    assert "Please fix the errors in the form below" in content
    assert "This field is required." in content


@pytest.mark.django_db
def test_form_missing_email(client):
    """If we submit the form without an email, we should see an
    appropriate error messages."""

    data = {
        'username': 'bartsimpson',
        'password1': 'Django123',
        'password2': 'Django123',
    }

    response = client.post(reverse('signup'), data=data, follow=True)

    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')
    assert "Please fix the errors in the form below" in content
    assert "This field is required." in content


@pytest.mark.django_db
def test_form_malformed_email(client):
    """If we submit the form with an email that is malformed, we should
    see an appropriate error messages.

    """

    data = {
        'username': 'bartsimpson',
        'email': 'bartsimpson',
        'password1': 'Django123',
        'password2': 'Django123',
    }

    response = client.post(reverse('signup'), data=data, follow=True)

    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')

    assert "Please fix the errors in the form below" in content
    assert "Enter a valid email address." in content


@pytest.mark.django_db
def test_form_missing_password1(client):
    """If we submit the form missing password1, we should
    see an appropriate error messages.

    """

    data = {
        'username': 'bartsimpson',
        'email': 'bart@simpsons.com',
        'password2': 'Django123',
    }

    response = client.post(reverse('signup'), data=data, follow=True)

    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')

    assert "Please fix the errors in the form below" in content
    assert "This field is required." in content


@pytest.mark.django_db
def test_form_missing_password2(client):
    """If we submit the form missing password2, we should
    see an appropriate error messages.

    """

    data = {
        'username': 'bartsimpson',
        'email': 'bart@simpsons.com',
        'password2': 'Django123',
    }

    response = client.post(reverse('signup'), data=data, follow=True)

    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')

    assert "Please fix the errors in the form below" in content
    assert "This field is required." in content


@pytest.mark.django_db
def test_form_password_mismatch(client):
    """If we submit the form with mis-matched passwords, we should
    see an appropriate error messages.

    """

    data = {
        'username': 'bartsimpson',
        'email': 'bart@simpsons.com',
        'password1': '123Django',
        'password2': 'Django123',
    }

    response = client.post(reverse('signup'), data=data, follow=True)

    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')

    assert "Please fix the errors in the form below" in content
    assert "The two password fields didn&#39;t match" in content


@pytest.mark.django_db
def test_form_short_password(client):
    """If we submit the form with a password that is too short, we should
    see an appropriate error messages.

    """

    data = {
        'username': 'bartsimpson',
        'email': 'bart@simpsons.com',
        'password1': '2short',
        'password2': '2short',
    }

    response = client.post(reverse('signup'), data=data, follow=True)

    assert 'signup.html' in [t.name for t in response.templates]
    assert response.status_code == 200

    content = response.content.decode('utf-8')

    assert "Please fix the errors in the form below" in content
    assert "This password is too short." in content
    assert "This password is too common." in content


@pytest.mark.django_db
def test_form_existing_username(client):
    """If we submit the form with a username that already exists, we should
    see an appropriate error messages.

    """
    assert 0 == 1


@pytest.mark.django_db
def test_form_existing_email(client):
    """If we submit the form with a email that already exists, we should
    see an appropriate error messages.

    """
    assert 0 == 1
