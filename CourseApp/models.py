from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=100, null=False, unique=True)
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
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True


# N.B name small letter
class tag(courseProperty_inheritance):
    pass


class prerequisite(courseProperty_inheritance):
    pass


class learning(courseProperty_inheritance):
    pass


class video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100, null=False)
    is_preview = models.BooleanField()

    def __str__(self):
        return self.title
