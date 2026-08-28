from django.shortcuts import render
from .models import Job


def job_list(request):
    jobs = Job.objects.all()

    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(job_id=job_id)

    return render(request, 'jobs/job-detail.html', {'job': job})