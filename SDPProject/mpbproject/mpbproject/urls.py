"""mpbproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.homifunction,name="home"),
    path("home",views.homepage,name="homepage"),
    path("demo",views.demofunction,name="demo"),
    path("index",views.indexfunction,name="index"),
    path("login",views.login,name="login"),
    path("sdphome",views.sdplogin,name="sdphome"),
    path("user",views.pawnbrokerfunction,name="pawnbroker"),
    path("pawnbroker",views.userfunction,name="user"),
    path("skhome",views.skfunction,name="skhome"),
    path("contact",views.contactfunction,name="contact"),

    path('admin/', admin.site.urls),
    path("prodemo/", include("prodemo.urls")),


]