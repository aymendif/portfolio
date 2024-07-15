from django.shortcuts import render
from .models import jobs
def nick(request):
    jobss=jobs.objects
    return render(request,'jobs/home.html',{'jobs':jobss}) 
    # Create your views here.
def default(request):
    return render(request,'jobs/default.html') 
    # Create your views here.
