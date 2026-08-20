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

def helloworld(request):
     debug_string = "<br>".join(f"<b>{k}</b>: {v}" for k, v in request.META.items())
    return HttpResponse(debug_string, content_type="text/html")
