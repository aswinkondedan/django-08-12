from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.TestFun,name='home'),
    path('about',views.TestFun,name='about'),
    path('contact',views.TestContact,name='contact'),
]