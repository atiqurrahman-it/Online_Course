from django.shortcuts import render, HttpResponse, redirect

from .models import Course, video
from user_app.models import User_select_course

from django.contrib.auth.decorators import login_required


# Create your views here.

def Homepage(request):
    all_course = Course.objects.filter(active=True)
    data = {
        "all_course": all_course
    }
    return render(request, 'pages/index.html', data)


def singleCoursePage(request, slug):
    single_course = Course.objects.get(slug=slug)
    all_video = single_course.video_set.all().order_by("serial_number")  # serial_number import
    serial_number = request.GET.get("lecture")  # import CourseSinglePage
    next_lecture = 2
    Previous = None
    if serial_number is None:
        serial_number = 1
    else:
        next_lecture = int(serial_number) + 1
        if len(all_video) < next_lecture:
            next_lecture = None

        Previous = int(serial_number) - 1

    link_click_video = video.objects.get(serial_number=serial_number, course=single_course)

    if link_click_video.is_preview is False:
        if request.user.is_authenticated is False:
            return redirect('login')
        else:
            user = request.user
            try:
                user_select_course = User_select_course.objects.get(user=user, course=single_course)
            except:
                # slug provide korte hobe path a
                return redirect('Enroll_checkout', slug=slug)

    data = {
        "singleCourse": single_course,
        "video_details": link_click_video,
        "all_video": all_video,
        "next_lecture": next_lecture,
        "Previous": Previous,
    }
    return render(request, 'pages/CourseSinglePage.html', data)


@login_required(login_url='login')
def MyCourses(request):
    current_user = request.user
    user_enroll_course = User_select_course.objects.filter(user=current_user)
    context = {
        "user_enroll_course": user_enroll_course,
    }
    return render(request, 'courseApp/my_courses.html', context)

# or
# from django.views.generic.list import ListView
# from django.utils.decorators import method_decorator
#
#
# @method_decorator(login_required(login_url='login'), name='dispatch')
# class MyCourses(ListView):
#     template_name = 'courseApp/my_courses.html'
#     context_object_name = 'user_enroll_course'

#
#     def get_queryset(self):
#         return User_select_course.objects.filter(user=self.request.user)
