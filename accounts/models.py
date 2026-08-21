from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        EMPLOYER = "employer", "Employer"
        EMPLOYEE = "employee", "Employee"

    role = models.CharField(
        max_length=20,
        choices=Role.choices
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    # accounts/models.py

class EmployerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer_profile"
    )

    company_name = models.CharField(max_length=200)

    company_website = models.URLField(
        blank=True
    )

    position = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.company_name


class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee_profile"
    )

    occupation = models.CharField(
        max_length=100,
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    available_for_work = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.user.get_full_name()