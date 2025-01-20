# myapp/models.py
from django.db import models

class JobApplication(models.Model):
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about_role = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.job_title




