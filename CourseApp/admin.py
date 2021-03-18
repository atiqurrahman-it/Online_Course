from django.contrib import admin
from .models import Course, Tag, prerequisite, Learning, Video


# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag


class prerequisiteAdmin(admin.TabularInline):
    model = prerequisite


class LearningAdmin(admin.TabularInline):
    model = Learning


class course_video_admin(admin.TabularInline):
    model = Video


class Course_Admin(admin.ModelAdmin):
    class Meta:
        model = Course

    inlines = [TagAdmin, prerequisiteAdmin, LearningAdmin, course_video_admin]


admin.site.register(Course, Course_Admin)

admin.site.register(Video)
