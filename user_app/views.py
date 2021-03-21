from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from CourseApp.models import Course
from user_app.models import Payment

from OnlineCourse.settings import *
from time import time

import razorpay

client = razorpay.Client(auth=(KEY_ID, kEY_SECRET))


# Create your views here.
def Enroll_checkout_Page(request, slug):
    course = Course.objects.get(slug=slug)
    user = None
    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    if action == 'create_payment':
        amount = int((course.price - ((course.price * course.discount) / 100)) * 100)
        currency = "INR"  # INDIAN RUPI
        notes = {
            "email": user.email,
            "name": f'{user.first_name} {user.last_name}'
        }
        reciept = f"E_learning_atiqur-{int(time())}"

        order = client.order.create(
            {'receipt': reciept,
             'notes': notes,
             'amount': amount,
             'currency': currency
             }
        )

        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()

    data = {
        "course": course,
        "order": order,
        "user": user,
    }
    return render(request, 'userpage/Enroll_checkout_page.html', data)


def Signup_page(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        pas_length = len(password1)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, ' taken Username  ')
                return redirect('signup')
            if pas_length <= 7:
                messages.info(request, 'Password too short , at least 8 characters  !')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'taken email')
                return redirect('signup')
            else:
                x = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                             password=password1, )
                x.save()
                messages.success(request, 'Your Have successfully signup ')
                return redirect('homepage')
        else:
            messages.success(request, ' Password Not matching ')
            return redirect('signup')
        return redirect('/')

    else:
        return render(request, 'Userpage/signup.html')


def Login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login')
    return render(request, 'Userpage/login.html')


def LogOut_page(request):
    logout(request)
    return redirect('login')
