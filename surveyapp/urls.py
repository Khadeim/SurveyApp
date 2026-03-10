from ast import Delete
from django.urls import  path, include
from .views import *
from .api import router

urlpatterns = [
    path('', Home, name  = 'home'),
    path('addquestion/', AddQuestion, name = "add-question"),
    path("deletequestion", DeleteQuestion, name="delete-question"),
    path("editquestion", EditQuestion, name="edit-question"),
    path("useranswer", UserAnswer, name = "user-answer"),


    path('GetAllQuestions', GetAllQuestions.as_view()),
    path("GetQuestionOptions/<int:pk>/", GetQuestionOptions.as_view()),
    path('GetQuestionResponse/<int:pk>/', GetQuestionResponse.as_view())
]