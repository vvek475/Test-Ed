from django.urls import path
from .views import *

urlpatterns = [
    path('register',Register,name='register'),
    path('login',Login,name='login'),
    path('logout',Logout,name='logout'),
    path('profile',Profile,name='profile'),
    path('getTeacher',getTeachers,name='getteacher'),
    path('createTeacher',createTeachers,name='createTeacher'),
    path('updateTeacher/<str:tId>',updateTeachers,name='updateTeacher'),
    path('updateTeacherSubject/<str:tId>',updateTeacherSubject,name='updateTeacherSubject')
    
]
