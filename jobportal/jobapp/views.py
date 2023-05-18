from django.shortcuts import render,redirect
from .models import jobs,cust_data,application,email_newsletter

# Create your views here.
def index(request):
    jobs_list = jobs.objects.all()
    return render(request,'index.html',{'jobs': jobs_list})

def abc404(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about.html')

def category(request):
    return render(request,'category.html')

def contact(request):
    if request.method == 'POST':
        data = cust_data.objects.create(name = request.POST['name'], email = request.POST['email'], sub = request.POST['sub'], mes = request.POST['mes'])
        data.save()
        return redirect('/')
    else:
        return render(request,'contact.html')

def joblist(request):
    jobs_list = jobs.objects.all()
    return render(request,'job-list.html',{'jobs': jobs_list})

def testimonial(request):
    return render(request,'testimonial.html')

def jobdetail(request,pk = None):
    data = jobs.objects.get(id = pk)
    return render(request,'job-detail.html',{'jobdata': data})

def app(request):
    if request.method == "POST":
        data = application.objects.create(name = request.POST['name'],email = request.POST['email'],web = request.POST['web'],job_id = request.POST['job_id'], job_post = request.POST['job_post'],file = request.POST['file'],coverletter = request.POST['coverletter'])
        data.save()
        return redirect('/')
    else:
        return render(request,'contact.html')
    
def emails(request):
    if request.method == "POST":
        data = email_newsletter.objects.create(email = request.POST['email'])
        data.save()
        return redirect('/')
    else:
        return render(request,'/')