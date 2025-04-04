from django.db import models 

# Create your models here.
class Blog(models.Model):
    uname = models.CharField(max_length=64)
    post = models.CharField(max_length=2000, blank=True)
    community = models.CharField(max_length=100, blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)

class Person(models.Model):
    uname = models.CharField(max_length=64, blank=False, primary_key=True)
    image = models.ImageField(upload_to = '',default='images.jpg', blank=True)
    name = models.CharField(max_length=64, blank=False)
    tagline = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    dob = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=64, blank=True)
    year_studying_in = models.CharField(max_length=10)
    college = models.CharField(max_length=100, blank=True)
    community = models.CharField(max_length=100, blank=True, default="GNDU, Amritsar")
    website = models.CharField(max_length=1000, blank=True)
    github = models.CharField(max_length=1000, blank=True)
    linkedin = models.CharField(max_length=1000, blank=True)
    instagram = models.CharField(max_length=1000, blank=True)
    twiiter = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.uname} : {self.name}"
    
class Follower(models.Model):
    # Whom to follow
    uname = models.CharField(max_length=64)
    follower = models.ManyToManyField(Person, blank=True)
    follower_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.uname} is following {self.follower_number} these many people"