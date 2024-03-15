from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import RegistrationForm, UpdateUserForm
from .models import Registration

from django.contrib import messages


def registration(request):
    form=RegistrationForm()

    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('userlogin')
        else:
            return redirect('regfail')

    return render(request,"registration.html",{"form":form})

def userlogin(request):
    return render(request,"userlogin.html")

def regfail(request):
    return render(request,"regfail.html")

def checkuserlogin(request):
    emaild=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=Registration.objects.filter( Q(email=emaild) & Q(password=pwd) )
    print(flag)

    if flag:
        user=Registration.objects.get(email=emaild)
        print(user)
        print(user.id,user.username) #other fields also
        request.session["uname"]=user.username
        return render(request,"user.html",{"uname":user.username})
    else:
        msg="Login Failed"
        return render(request,"userlogin.html",{"msg":msg})

def userhome(request):
    username=request.session["uname"]
    print(username)
    return render(request,"userhome.html",{"uname":username})

def userlogout(request):
    return render(request,"userlogin.html")

def logout(request):
    return redirect('home')

def viewusers(request):
    userdata=Registration.objects.all()
    usercount=Registration.objects.count()
    return render(request,"viewusers.html",{"users":userdata,"count":usercount})

def updateuser(request):
    form = UpdateUserForm()

    if request.method == "POST":
        form = UpdateUserForm(request.POST)
        emailid=form.data["email"]
        pwd=form.data["password"]

        flag=Registration.objects.filter(email=emailid)

        if flag:
            Registration.objects.filter(email=emailid).update(password=pwd)
            msg = "Password Updated Successfully"
            return render(request,"updateuser.html",{"pwdform":form,"msg":msg})
        else:
            msg = "User  with entered MailID Not Found"
            return render(request, "updateuser.html", {"pwdform": form, "msg": msg})

    return render(request,"updateuser.html",{"pwdform":form})

