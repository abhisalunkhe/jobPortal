from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class jobs(models.Model):
    logo = models.ImageField(upload_to='company_logo')
    post = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    job_type = models.CharField(max_length=10)
    date_of_release = models.DateField()
    salary = models.IntegerField()
    job_desc = models.TextField()
    responsibility_desc = models.TextField()
    qualification_desc = models.TextField()
    
class cust_data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=30)
    mes = models.TextField()
    
class application(models.Model):
    job_id = models.IntegerField()
    job_post = models.CharField(max_length=50)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    web = models.CharField(max_length=100)
    file = models.FileField()
    coverletter = models.TextField()

class email_newsletter(models.Model):
    email = models.EmailField()