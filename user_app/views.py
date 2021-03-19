from django.shortcuts import render, HttpResponse
from .form import SignUpForm


# Create your views here.

def Signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    form = SignUpForm()
    data = {
        "form": form,
    }
    return render(request, 'Userpage/signup.html', data)


def Login_page(request):
    return render(request, 'Userpage/login.html')


def LogOut_page(request):
    return HttpResponse("logout page ")
