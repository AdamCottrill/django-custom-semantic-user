"""Forms for our CustomUser application."""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Subclass the UserCreationForm"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """Subclass the UserChangeForm"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "email")
