from django import template

register = template.Library()


@register.filter()
def money_format(value):
    try:
        if value is None:
            value = 0
        return f'{value:,}'
    except:
        return ''


@register.filter()
def range_stars_fill(num):
    return range(num)


@register.filter()
def range_stars(num):
    return range(5 - num)
