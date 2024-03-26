from django.contrib import admin
from .models import Job,Application,Contact,Testimonials,Emails


class jobData(admin.ModelAdmin):
    list_display = ['id', 'post', 'location', 'job_type', 'date_of_release', 'salary']

class applicationData(admin.ModelAdmin):
    list_display = ['job_id', 'job_post', 'name', 'email','link', 'web']

class contactData(admin.ModelAdmin):
    list_display = ['name', 'email', 'sub', 'mes']

class testimonialData(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession', 'comment']

class emailData(admin.ModelAdmin):
    list_display = ['id', 'email']

# Register your models here.
admin.site.register(Job, jobData)
admin.site.register(Application, applicationData)
admin.site.register(Contact, contactData)
admin.site.register(Testimonials, testimonialData)
admin.site.register(Emails, emailData)