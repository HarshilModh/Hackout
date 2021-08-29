from django.contrib import admin
from django.urls import path
from admission import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home.html',views.home,name="home"),
    path('result.html',views.result,name="result"),
    path('output.html',views.output,name="output")
]