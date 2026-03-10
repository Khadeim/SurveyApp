
from django import template
from surveyapp.models import *

register = template.Library()

from datetime import datetime

def option(question,nummber):
    print('question', question)
    print('option', nummber)
    question = Questions.objects.get(id = question.id)
    option_statement = Options.objects.filter(question = question)

    return option_statement[nummber-1]
register.filter(option)