from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def login(request):
    return render(request, 'first/login.html')

def signup(request):
    return render(request, 'first/signup.html')