from django.db.models.signals import post_save
from django.contrib.auth.models import Group,User
from .models import *

def student_profile(sender,instance,created,**kwargs):
    if created:
        print(instance.is_staff)
        if instance.is_staff:
            group,created = Group.objects.get_or_create(name='teacher')
            instance.groups.add(group)  
            Teachers.objects.create(user=instance)
        else:            
            group,created = Group.objects.get_or_create(name='student')
            instance.groups.add(group)
            Students.objects.create(user=instance)
        
post_save.connect(student_profile,sender=User)