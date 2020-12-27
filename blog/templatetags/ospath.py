from django import template
from os.path import splitext

register = template.Library()

@register.filter
def noext(url):
    url_name = splitext(url)[0]
    print(url_name)
    return url_name
