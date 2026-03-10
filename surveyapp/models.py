from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
    statement = models.TextField( default='', blank=True, null=True)

    def __str__(self):
        return self.statement


class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_text  = models.TextField( default="", blank=True, null=True)
    def __str__(self):
        return self.option_text
class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_selected = models.ForeignKey(Options, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.question.statement) + " | " + str(self.option_selected.option_text)