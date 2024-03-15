from django.http import HttpResponse
from django.shortcuts import render,redirect



def homepage(request):
    return render(request,"home.html")

def demofunction(request):
    return redirect("test1")

def indexfunction(request):
    return render(request,"index.html")

def registration(request):
    return render(request,"registration.html")

def login(request):
    return render(request,"login.html")

def sdplogin(request):
    return render(request,"sdphome.html")

def userfunction(request):
    return render(request,"user.html")

def pawnbrokerfunction(request):
    return render(request,"pawnbroker.html")

def skfunction(request):
    return render(request,"skhome.html")

def contactfunction(request):
    return render(request,"contact.html")

def homifunction(request):
    return render(request,"home.html")

def adminfunction(request):
    return HttpResponse("<b>WELCOME TO ADMIN PAGE</b>")



