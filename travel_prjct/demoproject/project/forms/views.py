import re
import django
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        pswd=request.POST['password']
        conpswd=request.POST['conpassword']
        if pswd == conpswd:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email address already exist')
                return redirect('register')
            else:

                user=User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=pswd)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords are not same')
            return redirect('register')

    return render(request,'register.html')  

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)  

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Invalid email or password')
            return redirect('login')

    return render(request,'login.html')                    

def logout(request):
    auth.logout(request) 
    return redirect('/')  