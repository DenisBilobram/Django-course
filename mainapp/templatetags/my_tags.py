from django import template

register = template.Library()

@register.filter(name='castom_reverse')
def castom_reverse(string):
    return string[::-1]
