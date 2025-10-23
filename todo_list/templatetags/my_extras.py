from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value, arg):
    """
    THIS CUTS ALL VALUES OG ARG FROM THE STRING!
    """ 
    return value.replace(arg, "")
