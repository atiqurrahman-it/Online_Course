# Generated by Django 3.1.6 on 2021-03-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0002_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
