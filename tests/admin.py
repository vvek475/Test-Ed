import imp
from typing import Text
from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Subjects)
admin.site.register(Questions)
admin.site.register(TestQuestions)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'questions':
            # print(self.formfield_for_foreignkey)
            parent_id = request.resolver_match.kwargs.get('object_id')
            if parent_id:
                kwargs["queryset"] = Questions.objects.filter(subjects=Test.objects.get(id=parent_id).subjects)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Test,TestAdmin)
admin.site.register(TestScore)
admin.site.register(Answers)
