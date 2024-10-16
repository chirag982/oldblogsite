from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path("user/<str:username>", views.home, name="home"),
    path("user/feed", views.feed, name="feed"),
    path("user/post/add", views.add, name="add"),
    path("profile", views.profile, name="profile"),
    path("user/profile/update", views.details, name="details")
]