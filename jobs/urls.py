from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
     path('job-list/', views.job_list, name='job_list'),
]