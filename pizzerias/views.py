from django.shortcuts import render
from .models import PizzeriasUser
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse, HttpResponseRedirect


def register(request):
    if request.method == "GET":
        return render(request, "pizzerias/register.html", {})
 
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    name = request.POST['name']
    address = request.POST['address']

    user = User.objects.create_user(
                                    username = username,
                                    password = password,
                                    email = email)
    user.save()
    pu = PizzeriasUser(user = user, name = name, address = address)
    pu.save()
    return HttpResponseRedirect("/pizzerias/login")
    

def login(request):
    if request.method == "GET":
        return render(request, "pizzerias/login.html", {})
    
    usr = request.POST['username']
    pswd = request.POST['password']

    user = authenticate(username=usr, password=pswd)
    if user:
        auth_login(request, user)
        return HttpResponseRedirect("/pizzerias/")
    
    return render(request, "pizzerias/login.html", {"error": "username or password is wrong"})

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/pizzerias/login")