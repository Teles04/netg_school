from django import template


register = template.Library()

@register.filter()
def do_float(value):
    return float(value)