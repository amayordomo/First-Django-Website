from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")

    return render (request, 'authentication/login.html')

def authlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect ('login')

@csrf_protect
def authregistration(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirmpassword = request.POST['confirm-password']
        username = request.POST['username']
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        email = request.POST['email']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email associated with an existing account")
            else:
                user = User.objects.create(username=username, email=email, first_name=firstname, last_name=lastname)
                user.set_password(password)
                user.save()
                messages.success(request, "Account successfully created")
                return redirect('login')
        else:
            messages.error(request, "Password and Confirm Password do not match")



    return render (request, 'authentication/registration.html')

def forgotpassword(request):
    return render (request, 'authentication/forget.html')