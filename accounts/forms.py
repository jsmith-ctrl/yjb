from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from .models import User, EmployeeProfile, EmployerProfile


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"autofocus": True}),
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )


class EmployeeSignupForm(UserCreationForm):
    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "List your skills"
            }
        )
    )

    available_for_work = forms.BooleanField(
        required=False,
        initial=True
    )

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "birth_date",
            "skills",
            "available_for_work",
            "password1",
            "password2",
        )

        widgets = {
            "birth_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }


class EmployerSignupForm(UserCreationForm):
    company_name = forms.CharField(
        max_length=200
    )

    position = forms.CharField(
        max_length=100,
        required=False
    )

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "birth_date",
            "company_name",
            "position",
            "password1",
            "password2",
        )

        widgets = {
            "birth_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }