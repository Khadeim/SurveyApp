from django.shortcuts import redirect, render
from django.template import context
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .models import *
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.


from .serializers import *

from rest_framework import viewsets

class GetAllQuestions(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    def get(self, request):
        dic = {}
        question_list = []
        question_dic = {}
        temp_dic = {}
        questions = Questions.objects.all()
        for question in questions:
            question_dic["id"] = str(question.id)
            question_dic["Text"] = question.statement
            question_list.append(question_dic)
            question_dic = {}

        temp_dic["Questions"] = question_list
        dic["consultations"] = temp_dic

        return Response([dic])
  
class GetQuestionOptions(generics.RetrieveUpdateDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionSerializer
    def get(self, request, pk):
        dic = {}
        answer_list = []
        answer_dic = {}
        dic["Question"] = pk
        try:
            question = Questions.objects.get(id = pk)
            options = Options.objects.filter(question = question)
            for option in options: 

                answer_dic['id'] = option.id
                answer_dic['Text'] = option.option_text
                answer_list.append(answer_dic)
                answer_dic = {}
            dic["Options"] = answer_list
        except:
            dic["Options"] = "No data found"
        return Response([dic])
class GetQuestionResponse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

    def get(self, request, pk):
        dic = {}
        answer_list = []
        answer_dic = {}
        dic["Question"] = pk
        try:
            question = Questions.objects.get(id = pk)
            options = Options.objects.filter(question = question)
            for option in options: 
                answer = Answers.objects.filter(option_selected = option)
                count = len(answer)
                answer_dic['id'] = option.id
                answer_dic['count'] = count
                answer_list.append(answer_dic)
                answer_dic = {}
            dic["Answers"] = answer_list
        except:
            dic["Answers"] = "No data found"
        return Response([dic])

@login_required(login_url='login')
def Home(request):
    context = {}
    allQuestions = Questions.objects.all()
    context["allQuestion"] = allQuestions
    if request.user.is_superuser:
        return render(request, template_name = "surveyapp/home.html", context=context)

    else:
        return render(request, template_name = "surveyapp/home.html", context=context)

def UserAnswer(request):
    print("saving answer")
    length  = request.POST.get("length")
    print("request post",request.POST, length)
    for i in range(0,int(length)):
        question_id = request.POST.get(f"question-id_{i+1}", None)
        option1 = request.POST.get(f"option1_{i+1}", None)
        option2 = request.POST.get(f"option2_{i+1}", None)
        option3 = request.POST.get(f"option3_{i+1}", None)
        if question_id:
            question = Questions.objects.get(id = int(question_id))
            option = Options.objects.filter(question = question)
            if option1:
                option = option[0]
            elif option2:
                option = option[1]
            elif option3:
                option = option[2]
            else:
                option = None

            if option:
                user = User.objects.get(id = request.user.id)
                answer = Answers.objects.create(
                    user = user,
                    question = question,
                    option_selected = option
                )
                answer.save()
                print("answer saved")
    return redirect("home")


def DeleteQuestion(request):
    print("deleting")
    question_id = request.POST.get("question-id")
    question = Questions.objects.get(id = int(question_id))
    question.delete()
    print("deleted")
    return redirect("home")

def EditQuestion(request):
    print("editing question")
    question_statement = request.POST.get("question")
    option1 = request.POST.get("option1")
    option2 = request.POST.get("option2")
    option3 = request.POST.get("option3")
    question_id = request.POST.get("question-id")
    question = Questions.objects.get(id = int(question_id))
    # question.delete()
    question.statement = question_statement
    question.save()
    options  = Options.objects.filter(question = question)
    i = 1
    for option in options:
        if i == 1:
            option.option_text = option1
            option.save()
        if i == 2:
            option.option_text = option2
            option.save()
        if i == 3:
            option.option_text = option3
            option.save()
        i+=1
    print("All option saved")
    return redirect("home")

def AddQuestion(request):
    print("Adding question")
    question_statement = request.POST.get("question")
    option1 = request.POST.get("option1")
    option2 = request.POST.get("option2")
    option3 = request.POST.get("option3")

    question = Questions.objects.create(
        statement = question_statement
    )
    question.save()
    option1 = Options.objects.create(
        question = question,
        option_text = option1
    )
    option1.save()
    option2 = Options.objects.create(
        question = question,
        option_text = option2
    )
    option2.save()
    option3 = Options.objects.create(
        question = question,
        option_text = option3
    )
    option3.save()
    print("All option saved")
    return redirect("home")