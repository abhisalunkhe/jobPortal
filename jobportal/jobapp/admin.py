from django.contrib import admin
from .models import jobs

class admin_feature_items(admin.ModelAdmin):
    list_display = ['id', 'post', 'location', 'job_type', 'date_of_release', 'salary']

# Register your models here.
admin.site.register(jobs,admin_feature_items)