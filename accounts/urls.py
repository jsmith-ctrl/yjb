from django.urls import path

from . import views


urlpatterns = [
    path("signup/employee/", views.employee_signup, name="employee_signup"),

    path("signup/employer/", views.employer_signup, name="employer_signup"),
]