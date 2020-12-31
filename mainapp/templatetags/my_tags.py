from django import template

register = template.Library()

@register.filter(name='castom_reverse')
def castom_reverse(string):
    return string[::-1]

@register.filter(name='add_attr')
def add_attr(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val

    return field.as_widget(attrs=attrs)
