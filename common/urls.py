from django.urls import URLPattern
from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('leaderboard/<str:tId>',LeaderBoard,name='leaderboard'),
    path('solution/<str:tId>',Solution,name='solution')
]