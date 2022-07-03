from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def home(request):
    return render(request,'homeContent.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None: 
            login(request,user)
            return redirect('/')
        else:
            messages.success(request,("Ther was an error in logging in try again..."))
            return redirect('/login')


    else:
        return render(request,'login_user.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("you ware loged out succesful..."))
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request,user)
            messages.success(request,("Your registration was succesfull"))
            return redirect('home')

    else:
        form = RegisterForm()
    
    return render(request,'register.html',{
        'form':form,
    })

def aboutUs(request):
    return render(request,'aboutUs.html')

def buyCripto(request):
    return render(request,'BuyCripto.html')


def trade(request):
    return render(request,'trade.html')

def markets(request):
    return render(request,'market.html')

def earn(request):
    return render(request,'earn.html')



# Create your views here.

