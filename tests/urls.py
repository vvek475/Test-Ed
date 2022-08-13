from django.urls import path
from .views import *

urlpatterns = [
    path('create',createTest,name='create'),
    path('addQuestions/<str:id>',addQuestions,name='addQuestions'),
    path('testSession/<str:tId>/<str:qId>/<str:index>',TestSession,name='testSession'),
    path('startTest/<str:tId>',startTest,name='startTest'),
    path('testScore/<str:tId>',TestScore,name='testScore'),
    path('createsubject',createSubjects,name="createSubject"),
    path('createQuestion',createQuestions,name='createQuestion'),
    path('testlist',TestList,name="testList"),
    path('list',TestListView.as_view(template_name='test/new.html'))
]
