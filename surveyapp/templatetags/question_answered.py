from atexit import register
from django import template
from django.contrib.auth.models import User
from django.db.models import Q
register = template.Library()
from surveyapp.models import *
def is_question_answered(question_id, user_id):
    question = Questions.objects.get(id = question_id)
    user = User.objects.get(id = user_id)
    answer = Answers.objects.filter(Q(question = question) & Q(user = user))
    print(answer)
    if answer.exists():
        return True
    return False

register.filter(is_question_answered)


def answer(question_id, user_id):
    question = Questions.objects.get(id = question_id)
    user = User.objects.get(id = user_id)
    answer_statement = Answers.objects.filter(Q(question = question) & Q(user = user))
    print(answer)
    if answer_statement.exists():
        return answer_statement[0].option_selected.option_text
    return False
register.filter(answer)