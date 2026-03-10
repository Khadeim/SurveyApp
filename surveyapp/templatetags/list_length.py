
from django import template
register = template.Library()

def list_length(list):
    return len(list)

register.filter(list_length)