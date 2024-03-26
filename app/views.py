from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Job,Application,Contact,Testimonials,Emails
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    testimonials = Testimonials.objects.all()
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'testimonials': testimonials
    }
    return render(request,'index.html',context)

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = User.objects.filter(email=email)
        if user:
            messages.error(request, 'User with this email already exists! Please use a different email.')
            return redirect('register')  
        else:
            if password == cpassword:
                newuser = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=username,
                    password=password
                )
                newuser.save()
                messages.success(request, 'User created Successfully!!! You can now Login.')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match.')
                return redirect('register')

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are logged in successfully!!!')
            return redirect('/')
        else:
            messages.error(request,'Invalid credintials!!! Please check the credintials.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    messages.warning(request,'Logged out successfully!!! See you next time!')
    return redirect('login')

def about(request):
    return render(request,'about.html')

def jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request,'jobs.html',context)

@login_required(login_url='/login/')
def detail(request,pk = None):
    postdata = Job.objects.get(id = pk)
    username = request.user.username if request.user.is_authenticated else None
    context = {
        'data': postdata, 'username': username
    }
    return render(request, 'details.html', context)

@login_required(login_url='/login/')
def application(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        web = request.POST['web']
        job_id = request.POST['job_id']
        job_post = request.POST['job_post']
        link = request.POST['link']
        coverletter = request.POST['coverletter']
        data = Application.objects.create(name = name,email = email,web = web,job_id = job_id, job_post =job_post,link = link,coverletter = coverletter)
        data.save()
        return redirect('/')
    else:
        return render(request,'contact.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        data = Contact.objects.create(name=name,email=email,sub=subject,mes=message)
        data.save()
        return redirect('/')
    else:
        return render(request, 'contact.html')
    

def emails(request):
    if request.method == "POST":
        email = Emails.objects.create(email = request.POST['email'])
        email.save()
        messages.success(request, 'Successfully subscribed to our newsletter!!!')
        return redirect('/')
    else:
        return render(request,'/')