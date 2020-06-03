from django import template

register = template.Library()


@register.simple_tag(name = 'multiply')
def multiply(a, b, *args, **kwargs):
    # you would need to do any localization of the result here
    return round(a * b,2)