from django.db import models
from django.contrib.auth.models import User
from tests.models import Subjects

# Create your models here.
class Teachers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subjects=models.ManyToManyField(Subjects)
    date_joined=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Students(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_joined=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username