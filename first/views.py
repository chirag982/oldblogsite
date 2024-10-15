from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'beforelogin/index.html')

@login_required
def add(request):
    if request.method == "POST":
        username = request.user.username
        blog = request.POST["post"]
        post = Blog.objects.create(uname = username, post = blog)
        post.save()
        return redirect(reverse(home, args=[request.user.username]))
    return render(request, "afterlogin/add.html", {
        "username":request.user.username
    })

@login_required
def home(request, username):
    return render(request, "afterlogin/home.html", {
        "blog":Blog.objects.all()
    })

@login_required
def feed(request):
    return redirect(reverse(home, args=[request.user.username]))



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