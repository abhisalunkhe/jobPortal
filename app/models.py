from django.db import models

# Create your models here.

class Job(models.Model):
    logo = models.ImageField(upload_to='Company Logo')
    post = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    job_type = models.CharField(max_length=10)
    date_of_release = models.DateField()
    salary = models.IntegerField()
    job_desc = models.TextField()
    responsibility_desc = models.TextField()
    qualification_desc = models.TextField()

class Application(models.Model):
    job_id = models.IntegerField()
    job_post = models.CharField(max_length=50)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    web = models.CharField(max_length=100)
    link = models.CharField(max_length=80)
    coverletter = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=30)
    mes = models.TextField()

class Testimonials(models.Model):
    profile = models.ImageField(upload_to='Testimonial')
    name = models.CharField(max_length = 50)
    profession = models.CharField(max_length = 30)
    comment = models.CharField(max_length = 50)


class Emails(models.Model):
    email = models.EmailField()