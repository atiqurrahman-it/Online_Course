from django.contrib import admin
from django.utils.html import format_html

from .models import User_select_course, Payment


# Register your models here.

class User_select_course_admin(admin.ModelAdmin):
    pass


admin.site.register(User_select_course, User_select_course_admin)


class payment_admin(admin.ModelAdmin):
    list_display = ("order_id", "get_user_id", "get_coures", "status")

    def get_user_id(self, payment):
        return format_html(f"<a target='_blank'  href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")

    def get_coures(self, payment):
        return format_html(f"<a target='_blank' href='/admin/CourseApp/course/{payment.course.id}'>{payment.course}</a>")

    get_user_id.short_description = "User"
    get_coures.short_description = "course"


admin.site.register(Payment, payment_admin)
