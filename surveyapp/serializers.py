from rest_framework import serializers
from .models import *

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ["id","statement"]

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ["id","question", "option_text"]

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ["id", "question", "option_selected"]