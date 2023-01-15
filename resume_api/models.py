from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=32, blank=False)
    email = models.CharField(max_length=32, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    resume_url = models.TextField(blank=False)
    recruiter_notes = models.TextField(blank=True)
    recruiter_accepted = models.BooleanField()


### to view in python shell
# from resume_api.models import Resume
# for resume in Resume.objects.all():
#     print(resume.name)
#     print(resume.email)
#     print(resume.phone)
#     print(resume.resume_url)
#     print(resume.recruiter_notes)
#     print(resume.recruiter_accepted)