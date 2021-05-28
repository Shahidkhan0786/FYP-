from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blogHome"),
    path('display-post/<int:id>/', views.post_detail, name="displaypost"),
    path('/search/', views.post_Search, name="postserch"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

]
