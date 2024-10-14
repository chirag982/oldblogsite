from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'beforelogin/index.html')

def login(request):
    return render(request, 'beforelogin/login.html')

def signup(request):
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
                "message": "User created Successfully.",
                "username": user.username
            })    
    else:
        return render(request, 'beforelogin/signup.html')