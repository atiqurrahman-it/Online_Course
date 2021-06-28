from django.db import models

from django.contrib.auth.models import User
from CourseApp.models import Course


# Create your models here.

class User_select_course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} + {self.course.name}'


class Payment(models.Model):
    order_id = models.CharField(max_length=50, null=False)
    payment_id = models.CharField(max_length=50)
    user_sel_course = models.ForeignKey(User_select_course, on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
