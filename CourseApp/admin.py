from django.contrib import admin
from .models import Course, tag, prerequisite, learning, video


# Register your models here.
class TagAdmin(admin.TabularInline):
    model = tag


class prerequisiteAdmin(admin.TabularInline):
    model = prerequisite


class LearningAdmin(admin.TabularInline):
    model = learning


class course_video_admin(admin.TabularInline):
    model = video


class Course_Admin(admin.ModelAdmin):
    class Meta:
        model = Course

    inlines = [TagAdmin, prerequisiteAdmin, LearningAdmin, course_video_admin]
    list_display = ["click", "name", "get_price", "get_discount", "active"]
    list_filter = ("discount", "active")

    def get_discount(self, course):
        return f'{course.discount} %'

    def get_price(self, course):
        return f'৳ {course.price}'

    def click(self, course):
        return "click to Open "

    get_discount.short_description = "Discount"
    get_price.short_description = "Price"


admin.site.register(Course, Course_Admin)

admin.site.register(video)
