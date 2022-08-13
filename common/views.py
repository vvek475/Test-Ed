from django.shortcuts import render
from tests.models import *
from utilities.helpers import setRedirectUrl
from django.contrib.auth.decorators import login_required
# Create your views here.

@setRedirectUrl
@login_required(login_url='login')
def home(request):
    tests=Test.objects.all()[:5]
    userTest=TestScore.objects.filter(user=request.user)
    context={'tests':tests,'userTest':userTest}
    return render(request,'common/home.html',context)

@setRedirectUrl
@login_required(login_url='login')
def LeaderBoard(request,tId):
    test=Test.objects.get(id=tId)
    tests=TestScore.objects.filter(test=test).order_by('-score')[:10]
    userTest=TestScore.objects.filter(user=request.user,test=test)
    context={'tests':tests,'userTest':userTest[0] if len(userTest)>0 else False}
    return render(request,'common/leaderboard.html',context)

@setRedirectUrl
@login_required(login_url='login')
def Solution(request,tId):
    test=Test.objects.get(id=tId)
    questions=test.questions.all()
    userQuestions=TestQuestions.objects.filter(test=test,user=request.user)
    solutions=[]
    for i,j in zip(questions,userQuestions):
        solutions.append({'question':i.question,
             'answer':i.answer.answer,
             'userAnswer':j.answer.answer,
             'isCorrect':True if i.answer==j.answer else False})
    context={'solutions':solutions}
    return render(request,'common/solution.html',context)