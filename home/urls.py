from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
   path("", views.home, name='home'),
   path("home", views.home, name='home'),
   path("pictures", views.pictures, name='pictures'),
   path("contact", views.contact, name='contact'),
   path("about", views.about, name='about'),
   path("report", views.report, name='report'),
   path("blog", views.blog, name='blog'),
]
