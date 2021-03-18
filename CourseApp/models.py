from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=0, null=False)
    discount = models.IntegerField(default=0, null=False)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='thumbnail')
    resource = models.FileField(upload_to="resource")
    course_length = models.IntegerField(default=0, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class courseProperty_inheritance(models.Model):
    description = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True


class Tag(courseProperty_inheritance):
    pass


class prerequisite(courseProperty_inheritance):
    pass


class Learning(courseProperty_inheritance):
    pass


class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100, null=False)
    is_preview = models.BooleanField()
