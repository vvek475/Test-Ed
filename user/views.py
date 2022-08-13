from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from tests.models import Subjects, TestScore
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user.decorators import authenticatedRedirect
from user.models import Teachers
from utilities.helpers import setRedirectUrl,formerrorsHandler, unAuthorizedRedirect
from .forms import *
# Create your views here.
@authenticatedRedirect
def Register(request):
    print('passed')
    print(request.POST)
    form = UserRegistrationForm()
    if request.method=="POST":
        print(request.POST)
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'user/register.html',context)

@authenticatedRedirect
def Login(request):
    errors=False
    if request.method=="POST":
        user=authenticate(request,username=request.POST['username'],password=request.POST['pwd'])
        if user:
            login(request,user)
            return redirect('home')
        else:
            errors={'message':"Username and Password didn't match"}
    context={'errors':errors}
    return render(request,'user/login.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['admin'])
def getTeachers(request):
    teachers=Teachers.objects.all()
    teachersObj=[]
    for i in teachers:
        teachersObj.append({'name':i.user.username,
                        'subjects':i.subjects.all()[0] if len(i.subjects.all())>0 else None,
                        'tId':i.id,
                        'uId':i.user.id})
    context={'teachers':teachersObj}
    return render(request,'user/getteacher.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['admin'])
def createTeachers(request):
    form = UserRegistrationForm()
    if request.method=="POST":
        print(request.POST)
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'user/createTeacher.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['admin'])
def updateTeachers(request,tId):
    user=User.objects.get(id=tId)
    teacher=False
    subjects=Subjects.objects.all()
    if user.is_staff:
        teacher=user.teachers_set.all()[0]
    form = UserRegistrationForm(instance=user)
    if request.method=="POST":
        print(request.POST)
        form=UserRegistrationForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form,'user':user,'teacher':teacher,'subjects':subjects}
    return render(request,'user/updateTeacher.html',context)

@setRedirectUrl
@unAuthorizedRedirect(allowedRoles=['admin'])
def updateTeacherSubject(request,tId):
    user=User.objects.get(id=tId)
    if user.is_staff:
        teacher=user.teachers_set.all()[0]
    if request.method=='POST':
        form=Teacherform(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
        else:
            messages.error(request,formerrorsHandler(form.errors))
    return redirect('updateTeacher',tId)

@setRedirectUrl
@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

@setRedirectUrl
@login_required(login_url='login')
def Profile(request):
    tests=TestScore.objects.filter(user=request.user)
    context={'tests':tests}
    return render(request,'user/profile.html',context)