from django import template

register = template.Library()

@register.filter
def to_and(value):
    value=value.replace("and", " and ")
    return value