from django.shortcuts import render

# Create your views here.

def default(request):
    # Optional: Context dictionary containing data passed to the HTML template
    context = {
        "page_title": "Home Page",
        "items": ["Python", "Django", "Boilerplate"],
    }

    # Renders 'myapp/index.html' with the context data
    return render(request, "yjb/default.html", context)
