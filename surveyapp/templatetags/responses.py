from atexit import register
from django import template
from django.contrib.auth.models import User
from django.db.models import Q

register = template.Library()
from surveyapp.models import *
def total_answers(question_id):
    total_given_answers = Answers.objects.filter(question = question_id)
    return len(total_given_answers)
register.filter(total_answers)

def total_answers_option(question_id, option_number):
    all_options = Options.objects.filter(question = question_id)
    option = all_options[option_number-1]
    total_option_selected = Answers.objects.filter(option_selected = option)
    return len(total_option_selected)
register.filter(total_answers_option)