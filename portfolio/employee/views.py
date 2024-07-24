from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def employeeHome(request):
    return HttpResponse("This is our employee home")

def profile(request):
    return render(request, 'employee/profile.html')