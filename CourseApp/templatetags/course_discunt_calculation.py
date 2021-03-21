from django import template

register = template.Library()

import math


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
    return f'{main_price} TK'

# f thats meens formeting
