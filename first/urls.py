from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("about", views.about, name="about"),
    path("find", views.find, name="find"),
    path("SearchedFor/<str:check>", views.people, name="people"),
    path("check", views.check, name="check"),
    path("user/<str:username>", views.home, name="home"),
    path("user/feed", views.feed, name="feed"),
    path("posts", views.myposts, name="myposts"),
    path("user/post/add", views.add, name="add"),
    path("profile", views.profile, name="profile"),
    path("user/profile/update", views.details, name="details")
]