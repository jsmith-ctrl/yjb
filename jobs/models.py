from django.db import models

# Create your models here.

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    commitment = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    requirements = models.TextField()   
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self): 
        return self.title
   