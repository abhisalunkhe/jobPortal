from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('jobs/',views.jobs,name='jobs'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('contact/',views.contact,name='contact'),
    path('detail/application',views.application,name='application'),
    path('emails',views.emails,name='emails'),
]
