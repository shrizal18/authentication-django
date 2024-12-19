from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    return render(request, "homepage.html")

def signup(request):
    form =UserCreationForm()
    if request.method =="POST":
        print(request.POST)
        name= request.POST.get("name")
        email= request.POST.get("email")
        username= request.POST.get("username")
        password= request.POST.get("password")
        con_pass= request.POST.get("con_pass")

        if con_pass != password:
            messages.error(request, "Password not matched")

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username not available")

        else :
            user = User.objects.create_user(username=username ,email=email )
            user.set_password(password)
            user.save()
            return redirect("/login")
        
    return render (request, "signup.html" , context={"form": form})

def log_out(request):
    logout(request=request)
    return redirect("/")

def log_in(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username):
            messages.error(request, "Username doesn't exist")
            return render(request, "login.html")
        else:
            user= authenticate(request, username=username , password=password)
            if user is None:
                messages.error(request,"Invalid User")
                return render(request, "login.html")
            else:
                login(request=request,user=user)
                return redirect("/")
    return render(request, "login.html")

from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def profile(request):
    return render(request, "profile.html")