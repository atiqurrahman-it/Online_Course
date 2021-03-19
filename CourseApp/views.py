from django.shortcuts import render, HttpResponse
from .models import Course, video


# Create your views here.

def Homepage(request):
    all_course = Course.objects.all()
    data = {
        "all_course": all_course
    }
    return render(request, 'pages/index.html', data)


def singleCoursePage(request, slug):
    print(request.user.is_authenticated)
    print(request.user)
    single_course = Course.objects.get(slug=slug)
    all_video = single_course.video_set.all().order_by("serial_number")  # serial_number import
    serial_number = request.GET.get("lecture")  # import CourseSinglePage
    if serial_number is None:
        serial_number = 1
    link_click_video = video.objects.get(serial_number=serial_number, course=single_course)

    data = {
        "singleCourse": single_course,
        "video_details": link_click_video,
        "all_video": all_video,
    }
    return render(request, 'pages/CourseSinglePage.html', data)
