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
    path("signup", views.Signup_page, name='signup'),
    path("login", views.Login_page, name='login'),
    path("logout", views.LogOut_page, name='logout'),
    path("Enroll_checkout/<str:slug>", views.Enroll_checkout_Page, name='Enroll_checkout'),
    path("veryfy_payment", views.verifyPayment, name='verifyPayment'),
]
