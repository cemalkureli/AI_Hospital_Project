from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout 
from user.forms import DoctorRegisterForm,DoctorLoginForm
from user.models import RegisterDoctor

# Create your views here.


def register(request):
    form = forms.RegisterForm(request.POST or None) 
                                                                                                                          
    if form.is_valid(): 
        username = form.cleaned_data.get("username") 
        password = form.cleaned_data.get("password")
        name = form.cleaned_data.get("name")
        surname = form.cleaned_data.get("surname")
        email = form.cleaned_data.get("email")
        
        newUser = User(username = username) 
        newUser.set_password(password)
        newUser.first_name = name
        newUser.last_name = surname
        newUser.email = email

        newUser.save()
        login(request,newUser)
        messages.success(request, "You Have Successfully Registered")  # Django Messages -->  https://docs.djangoproject.com/en/4.1/ref/contrib/messages/ 
        return redirect("home") 

    context = {
        "form": form,
    }
    return render(request,"register.html",context) 


def loginUser(request):
    form = forms.LoginForm(request.POST or None)

    context = {
        "form" : form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username") 
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Username or Password is Invalid")
            return render(request,"login.html",context)
    
        login(request,user)
        messages.info(request, "You Have Successfully Logged in")
        return redirect("home")

    return render(request,"login.html",context) 


def logoutUser(request):
    logout(request)
    messages.info(request, "You Have Successfully Logged out")
    return redirect("home")




def doctor_register(request):
    form = DoctorRegisterForm(request.POST or None) 
                                                                                                                          
    if form.is_valid():
        name = form.cleaned_data.get("name")
        surname = form.cleaned_data.get("surname")
        email = form.cleaned_data.get("email") 
        password = form.cleaned_data.get("password")
        phone_number = form.cleaned_data.get("phone_number")
        address = form.cleaned_data.get("address")
        gender = form.cleaned_data.get("gender")
        department = form.cleaned_data.get("department")
        degree = form.cleaned_data.get("degree")
        birth_date = form.cleaned_data.get("birth_date")
        
        new_user = User.objects.create_user(username=email, email=email, password=password, first_name=name, last_name=surname)
        new_user.save()
        login(request, new_user)


        new_doctor = RegisterDoctor.objects.create(
        user=new_user,name=name, surname=surname, email=email, password=password, phone_number=phone_number,
        address=address, gender=gender, department=department, degree=degree, birth_date=birth_date)
        new_doctor.save()
        messages.success(request, "You Have Successfully Registered")  # Django Messages -->  https://docs.djangoproject.com/en/4.1/ref/contrib/messages/ 
        return redirect("home") 

    context = {
        "form": form,
    }
    return render(request,"doctor/register.html",context) 


def doctor_login(request):
    form = DoctorLoginForm(request.POST or None)

    context = {
        "form" : form,
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is None:
            messages.error(request, "Username or Password is Invalid")
            return render(request,"doctor/login.html",context)
        
        login(request,user)
        messages.info(request, "You Have Successfully Logged in")
        return redirect("home")

    return render(request,"doctor/login.html",context) 
