from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.db import transaction
from django.shortcuts import render, redirect

from .forms import AccountLoginForm, EmployeeSignupForm, EmployerSignupForm
from .models import User, EmployeeProfile, EmployerProfile


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = AccountLoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("home")

    return render(request, "accounts/login.html", {"form": form})


@transaction.atomic
def employee_signup(request):

    if request.method == "POST":
        form = EmployeeSignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.role = User.Role.EMPLOYEE
            user.save()

            EmployeeProfile.objects.create(
                user=user,
                skills=form.cleaned_data["skills"],
                available_for_work=form.cleaned_data["available_for_work"],
            )

            login(request, user)

            return redirect("home")

    else:
        form = EmployeeSignupForm()

    return render(
        request,
        "accounts/employee_signup.html",
        {"form": form}
    )


@transaction.atomic
def employer_signup(request):

    if request.method == "POST":
        form = EmployerSignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.role = User.Role.EMPLOYER
            user.save()

            EmployerProfile.objects.create(
                user=user,
                company_name=form.cleaned_data["company_name"],
                position=form.cleaned_data["position"],
            )

            login(request, user)

            return redirect("home")

    else:
        form = EmployerSignupForm()

    return render(
        request,
        "accounts/employer_signup.html",
        {"form": form}
    )