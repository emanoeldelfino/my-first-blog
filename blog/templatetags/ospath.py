from django import template
from os.path import splitext

register = template.Library()

@register.filter
def noext(url):
    url_name = splitext(url)[0]
    return url_name
