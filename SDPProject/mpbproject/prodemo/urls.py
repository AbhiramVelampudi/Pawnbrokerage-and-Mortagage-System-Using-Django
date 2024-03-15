from django.urls import path
from . import views

urlpatterns = [

    path("registration", views.registration, name="registration"),
    path("regfail", views.regfail, name="regfail"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("checkuserlogin", views.checkuserlogin, name="checkuserlogin"),
    path("userhome", views.userhome, name="userhome"),
    path("userlogout", views.userlogout, name="userlogout"),
    path("viewusers", views.viewusers, name="viewusers"),
    path("logout", views.logout, name="logout"),
    path("updateuser",views.updateuser,name="updateuser"),


    ]