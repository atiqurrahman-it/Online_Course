from django.shortcuts import render, HttpResponse
from .models import Course


# Create your views here.

def Homepage(request):
    all_course = Course.objects.all()
    data = {
        "all_course": all_course
    }
    return render(request, 'pages/index.html', data)


def singleCoursePage(request, slug):
    single_course = Course.objects.get(slug=slug)
    data = {
        "singleCourse": single_course
    }
    return render(request, 'pages/CourseSinglePage.html', data)
