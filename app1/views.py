from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('helooooooo')

def TestAbt(request):
    return HttpResponse('<h1>helooo test</h1>')
   
def TestContact(request):
    return render(request,'2.html')