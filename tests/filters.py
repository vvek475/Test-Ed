from turtle import title
import django_filters
from.models import *
class TestFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Test
        fields = ['teacher', 'subjects']