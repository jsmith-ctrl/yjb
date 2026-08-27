from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def default(request):
    # Optional: Context dictionary containing data passed to the HTML template
    context = {
        "page_title": "Home Page",
        "items": ["Python", "Django", "Boilerplate"],
    }

    # Renders 'myapp/index.html' with the context data
    return render(request, "yjb/default.html", context)

def home(request):
    return render(request, "yjb/home.html", {})

def job_listings(request):
    return render(request, "yjb/job-listings.html")

def about(request):
    return render(request, "yjb/about.html")

def contact(request):
    return render(request, "yjb/contact.html")

def applicants(request):
    return render(request, "yjb/employer/applicants.html")

def employee_signup(request):
    return render(request, "yjb/employee/sign-up-employee.html")

def employer_signup(request):
    return render(request, "yjb/employer/sign-up-employer.html")

def helloworld(request):
     debug_string = "<br>".join(f"<b>{k}</b>: {v}" for k, v in request.META.items())
     return HttpResponse(debug_string, content_type="text/html")

def job_detail(request):
    return render(request, "yjb/job-detail.html")