from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all()

    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(job_id=job_id)

    return render(request, 'jobs/job-detail.html', {'job': job})

def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save()

            return redirect('job_detail', pk=job.pk)

    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {
        'form': form
    })