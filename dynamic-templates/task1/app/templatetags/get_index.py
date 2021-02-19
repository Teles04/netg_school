from django import template


register = template.Library()

@register.filter()
def get_index(value):
    return float(value)