from django.urls import path

from . import views


urlpatterns = [
    path("login/", views.login_view, name="login"),

    path("signup/employee/", views.employee_signup, name="employee_signup"),

    path("signup/employer/", views.employer_signup, name="employer_signup"),
]