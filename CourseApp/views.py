from django.shortcuts import render
from .models import Course


# Create your views here.

def Homepage(request):
    all_course = Course.objects.all()
    data = {
        "all_course": all_course
    }
    return render(request, 'pages/index.html',data)
