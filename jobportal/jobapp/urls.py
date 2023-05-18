from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('abc404',views.abc404,name='abc404'),
    path('about',views.about,name='about'),
    path('category',views.category,name='category'),
    path('contact',views.contact,name='contact'),
    path('jobdetail/<int:pk>',views.jobdetail,name='jobdetail'),
    path('joblist',views.joblist,name='joblist'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('jobdetail/app',views.app,name='app'),
    path('emails',views.emails,name='emails'),
]