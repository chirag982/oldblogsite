from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Blog, Person

# Create your views here.
def index(request):
    return render(request, 'beforelogin/index.html')

@login_required
def find(request):
    if request.method == "POST":
        find = request.POST["find"]
        if Person.objects.filter(uname=find):
            p = Person.objects.get(uname=find)
            return render(request, "afterlogin/find.html", {
                "person": p
            })
        return render(request, "afterlogin/find.html", {
            "message":"No such user found! Please enter the correct username."
        })
    else:
        return render(request, "afterlogin/find.html")

@login_required
def people(request, check):
    p = Person.objects.get(uname=check)
    return render(request, "afterlogin/people.html", {
            "person":p
        })

@login_required
def check(request):
    if request.method == "POST":
        p = request.POST["check"]
        return redirect(people, check=p)
    else:
        return redirect(reverse(find))

@login_required
def about(request):
    return render(request, "afterlogin/about.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse(index))
    

@login_required
def profile(request):
    username = request.user.username
    person = Person.objects.get(uname = username)
    return render(request, "afterlogin/profile.html", {
        "person":person
    })

@login_required
def community(request):
    user = request.user.username
    person = Person.objects.get(uname = user)
    blog = Blog.objects.filter(community = person.community).order_by('-time')
    return render(request, "afterlogin/community.html",{
        "person":person,
        "blog":blog
    })

@login_required
def details(request):
    if request.method == "POST":
        uname = request.user.username
        image = request.FILES.get("image", None)    
        name = request.POST["name"]
        college = request.POST["college"]
        year = request.POST["year"]
        department = request.POST["department"]
        community = request.POST["community"]
        website = request.POST["website"]
        github = request.POST["github"]
        instagram = request.POST["instagram"]
        linkedin = request.POST["linkedin"]
        twitter = request.POST["twitter"]

        person = Person.objects.filter(uname=uname)
        p = Person.objects.get(uname=uname)
        p.name = name
        p.college = college
        p.year_studying_in = year
        p.department=department
        p.website = website
        p.community = community
        if image:
            p.image = image
        p.github=github
        p.instagram=instagram
        p.linkedin=linkedin
        p.twiiter= twitter
        p.save()
        return redirect(reverse(profile))
    else:
        username = request.user.username
        person = Person.objects.get(uname = username)
        return render(request, "afterlogin/details.html", {
            "person":person
        })

@login_required
def add(request):
    if request.method == "POST":
        uname = request.user.username
        person = Person.objects.get(uname = uname)
        blog = request.POST["post"]
        p = Blog.objects.create(uname=uname, post=blog, community=person.community).save()
        return redirect(reverse(home, args=[request.user.username]))
    return render(request, "afterlogin/add.html", {
        "username":request.user.username
    })

@login_required
def home(request, username):
    return render(request, "afterlogin/home.html", {
        "blog":Blog.objects.all().order_by('-time').values()
    })

@login_required
def myposts(request):
    username = request.user.username
    b = Blog.objects.filter(uname=username)
    return render(request, "afterlogin/myposts.html", {
        "blog": b
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
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        if (User.objects.filter(username=username).exists()):
            return render(request, 'beforelogin/signup.html', {
                        "message": "User already exists with this username"
                    })
        else:
            user = User.objects.create_user(username, email, password)
            person = Person.objects.create(uname = username, name=name, email = email)
            person.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect(reverse(details), {
                "message":"User created successfully and logined successfully"
            })    
    else:
        return render(request, 'beforelogin/signup.html')