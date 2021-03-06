"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.Homepage, name='homepage'),
    path("singleCourse/<str:slug>/", views.singleCoursePage, name='singleCourse'),
    path("my_courses", views.MyCourses, name='my_courses'),

]
