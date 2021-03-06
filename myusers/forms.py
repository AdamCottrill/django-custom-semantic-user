"""Forms for our CustomUser application."""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Subclass the UserCreationForm

    Note that e-mail is now a required field.
    """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class CustomUserChangeForm(UserChangeForm):
    """Subclass the UserChangeForm"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("first_name", "last_name", "email")
