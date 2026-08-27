
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from yjb.views import home
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yjb/', include('yjb.urls')),
    path('jobs/', include('jobs.urls')),
    path('', home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
