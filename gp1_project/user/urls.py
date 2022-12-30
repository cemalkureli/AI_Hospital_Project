from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("register/",views.register, name="register"),
    path("login/",views.loginUser, name="login"),
    path("logout/",views.logoutUser, name="logout"),
    path("doctorregister/",views.doctor_register, name="doctorregister"),
    path("doctorlogin/",views.doctor_login, name="doctorlogin"),
    path("doctorlogout/",views.logoutUser, name="doctorlogout"),


]