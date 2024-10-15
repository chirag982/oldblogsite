from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
    return render(request, 'beforelogin/index.html')


@login_required
def home(request, username):
    return render(request, "afterlogin/home.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse(home, args=[username]))
        else:
            return render(request, 'beforelogin/login.html', {
                "message": "Wrong Credentials."
            })
    else:
        return render(request, 'beforelogin/login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if (User.objects.filter(username=username).exists()):
            return render(request, 'beforelogin/signup.html', {
                        "message": "User already exists with this username"
                    })
        else:
            user = User.objects.create_user(username, email, password)
            return render(request, "beforelogin/login.html", {
                "message": "User created Successfully."
            })    
    else:
        return render(request, 'beforelogin/signup.html')