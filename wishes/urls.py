from django.urls import path , include
from .views import *
from wishes import views

urlpatterns = [
    path('', views.home),
    
]