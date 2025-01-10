from django.contrib import admin
from . models import Blog, Person, Follower

# Register your models here.
admin.site.register(Blog)
admin.site.register(Person)
admin.site.register(Follower)
