from django.shortcuts import render,redirect
from django.db.models import Avg,IntegerField
from tests.filters import TestFilter
from utilities.helpers import formerrorsHandler, setRedirectUrl, unAuthorizedRedirect
from .models import *
from .models import TestScore as testscore
from user.models import *
from django.contrib import messages

from tests.forms import *

# Create your views here.
@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['teacher','admin'])
def createSubjects(request):
    
    if request.method=="POST":
        form=CreateSubject(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Subject created')
        else:
            messages.error(request,formerrorsHandler(form.errors))
    return redirect('create')

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['teacher','admin'])
def createQuestions(request):
    if request.method=="POST":
        form=CreateQuestion(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Question created')
        else:
            messages.error(request,formerrorsHandler(form.errors))
    return redirect('create')
          
@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['teacher','admin'])
def createTest(request):
    form = CreateTestForm(initial={'teacher':request.user})
    questionForm=CreateQuestion()
    subjectForm=CreateSubject()
    if request.method=='POST':
        form=CreateTestForm(request.POST)
        if form.is_valid():
            saved=form.save()
            messages.success(request,'Test created')
            return redirect('/tests/addQuestions/'+str(saved.id))
        else:
            messages.error(request,formerrorsHandler(form.errors))
    context={'form1':subjectForm,'form2':questionForm,'form3':form}
    return render(request,'test/create.html',context)

    
@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['teacher','admin'])
def addQuestions(request,id):
    test=Test.objects.get(id=id)
    questions=Questions.objects.filter(subjects=test.subjects)
    form=AddQuestionsForm(instance=test)
    # [question['isselected'] for question in questions if question in test.questions.all()]
    for i in questions:
        if i in test.questions.all():
            i.istrue =True
        else:
            i.istrue=False   
    if request.method=='POST':
        form=AddQuestionsForm({'questions':request.POST.getlist('questions')},instance=test)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form,'questions':questions}
    return render(request,'test/add-questions.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['student','teacher','admin'])
def startTest(request,tId):
    test=Test.objects.get(id=tId)
    enrolled=testscore.objects.filter(test=test).count()
    qId=test.questions.all()[0]
    avg=testscore.objects.filter(test=test).aggregate(avg_score=Avg('score',output_field=IntegerField()))
    context={'test':test,'qId':qId,'index':0,'enrolled':enrolled,'questions':test.questions.all().count(),'avg':avg}
    return render(request,'test/startTest.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['student','teacher','admin'])
def TestSession(request,tId,qId,index):
    test=Test.objects.get(id=tId)
    questionsLength=len(test.questions.all())
    question=test.questions.all()[int(index)]
    answers=Questions.objects.get(id=qId).choices.all()
    testQuestion,_=TestQuestions.objects.get_or_create(test=test,question=question)
    if request.method=="POST":
        
        form=TestQuestionsForm({'answer':request.POST['answers'],
                               'user':request.user,
                               'question':question,
                               'test':test},instance=testQuestion)
        if form.is_valid():
            form=form.save()
            if int(index)>=questionsLength-1:
                return redirect(f'/tests/testScore/{tId}')
            else:
                return redirect(f'/tests/testSession/{tId}/{qId}/{int(index)+1}')
    context={'question':question,'index':index,'answers':answers}
    return render(request,'test/testSession.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['student','teacher','admin'])
def TestScore(request,tId):
    test=Test.objects.get(id=tId)
    listOfTestQuestions=TestQuestions.objects.filter(user=request.user,test=test)
    score=0
    questions=test.questions.all()
    testScore,_=testscore.objects.get_or_create(user=request.user,test=test)
    for i,j in zip(questions,listOfTestQuestions):
        if i.answer.id==j.answer.id:
            score+=1
    form=TestScoreForm({'user':request.user,
                              'score':score,
                              'test':test},instance=testScore)
    if form.is_valid():
        form.save()
    if request.method=='POST':
        return redirect('solution',test.id)
    context={'tId':test.id}
    return render(request,'test/testScore.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['student','teacher','admin'])
def TestList(request):
    testFilter=TestFilter(request.GET,queryset=Test.objects.all())
    subjects=Subjects.objects.all()
    teachers=Teachers.objects.all()
    context={'filter':testFilter,'subjects':subjects,'teachers':teachers}
    return render(request,'test/test.html',context)

# from django.views.generic import *
# class TestListView(ListView):
#     # template_name = 'test/new.html'
#     context_object_name= 'tests'
#     model=Test
#     queryset= Test.objects.filter(subjects=Subjects.objects.get(name='social'))
#     def get_context_data(self, **kwargs: any) -> dict[str, any]:
#         context= super(TestListView,self).get_context_data(**kwargs)
#         context['subject'] = 'science'
#         print(context)
        
#         return context