from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
     path('job-list/', views.job_list, name='job_list'),
     path('job-detail/<int:job_id>/', views.job_detail, name='job_detail'),
     path('post-job/', views.job_post, name='post_job')
]