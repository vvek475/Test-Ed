from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subjects(models.Model):
    name=models.CharField(max_length=10,unique=True)
    
    def __str__(self):
        return self.name
    
class Answers(models.Model):
    answer=models.CharField(max_length=10)
    
    def __str__(self):
        return self.answer
class Questions(models.Model):
    
    question=models.TextField(max_length=500)
    subjects=models.ForeignKey(Subjects,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(auto_now_add=True)
    score=models.IntegerField(default=1)
    answer=models.ForeignKey(Answers,on_delete=models.CASCADE,null=True,related_name='question_answer')
    choices=models.ManyToManyField(Answers,related_name='question_choices')
        
    def __str__(self):
        return self.question
    
class Test(models.Model):
    title=models.CharField(max_length=50)
    questions=models.ManyToManyField(Questions,blank=True,default=None)
    attempts=models.IntegerField(default=1)
    subjects=models.ForeignKey(Subjects,null=True,on_delete=models.CASCADE)
    teacher=models.ForeignKey('user.Teachers',on_delete=models.CASCADE,null=True,related_name='teacher')
    
    def __str__(self):
        return self.title
    
class TestQuestions(models.Model):
    test=models.ForeignKey(Test,null=True,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,null=True,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    answer=models.ForeignKey(Answers,on_delete=models.CASCADE,null=True,related_name='test_answer')
    
    def __str__(self) -> str:
        return self.question.question
    
class TestScore(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    score=models.IntegerField(default=0,null=True)
    test=models.ForeignKey(Test,null=True,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username