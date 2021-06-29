from django import template

register = template.Library()

import math

from user_app.models import User_select_course


# https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/

@register.simple_tag
def cou_dis_cal(main_price, discount):
    if discount is None or discount is 0:
        return main_price
    sell_price = main_price
    sell_price = main_price - ((main_price * discount) / 100)
    return math.floor(sell_price)


@register.filter
def Taka(main_price):
    return f'{main_price} $'


# f thats meens formeting


# course enroll ache ki na check korbe

@register.simple_tag
def isCourseEnroll(request, course):
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    try:
        user_select_course = User_select_course.objects.get(user=user, course=course)
        return True
    except:
        return False
