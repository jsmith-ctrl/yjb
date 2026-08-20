from django.contrib import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path('default/', views.default, name='default'),
    path('job-listings/', views.job_listings, name='job_listing'),
    path('employee-signup/', views.employee_signup, name='employee_signup'),
    path('employer-signup/', views.employer_signup, name='employer_signup'),
    path('applicants/', views.applicants, name='applicants'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')

]
