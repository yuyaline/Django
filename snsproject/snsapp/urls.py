from django.contrib import admin
from django.urls import path,include
from .views import signupfunc,loginfunc,listfunc

urlpatterns = [
    path("signup/",signupfunc,name="signup"),
    path("login/",loginfunc,name="login"),
    path("list/",listfunc,name="list"),
]
