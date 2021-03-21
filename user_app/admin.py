from django.contrib import admin
from .models import User_select_course, Payment


# Register your models here.

class User_select_course_admin(admin.ModelAdmin):
    pass


admin.site.register(User_select_course, User_select_course_admin)


class payment_admin(admin.ModelAdmin):
    pass


admin.site.register(Payment, payment_admin)
