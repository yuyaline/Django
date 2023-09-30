from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login

def signupfunc(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.create_user(username,"",password)
            return render(request,"signup.html",{"some":"somess"})
        except IntegrityError:
            return render(request,"signup.html",{"error":"このユーザーは既に登録されています"})

    return render(request,"signup.html")

def loginfunc(request):
    if request.method == "POST": 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request,"login.html",{"context":"login"})
        else:
            return render(request,"login.html",{"context":"not login"})

    return render(request,"login.html",{"context":"get method"})

def listfunc(request):
    return render(request,"list.html",{"context":"list"})