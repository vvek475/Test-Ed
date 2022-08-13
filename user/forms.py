from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms

from user.models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','is_staff']
        
class Teacherform(forms.ModelForm):
    class Meta:
        model=Teachers
        fields=['subjects']