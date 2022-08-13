from django.forms import ModelForm
from .models import *

class CreateSubject(ModelForm):
    class Meta:
        model=Subjects
        fields='__all__'
        
class CreateQuestion(ModelForm):
    class Meta:
        model=Questions
        fields='__all__'
        
class CreateTestForm(ModelForm):
    class Meta:
        model=Test
        fields='__all__'
        exclude=['questions']
        
class AddQuestionsForm(ModelForm):
    class Meta:
        model=Test
        fields=['questions']
    def __init__(self, *args, **kwargs):
        # current_user = kwargs.pop('Subjects')
        try:
            super(AddQuestionsForm, self).__init__(*args, **kwargs)
            self.fields['questions'].queryset = kwargs['instance']
        except:
            pass
        
class TestQuestionsForm(ModelForm):
    class Meta:
        model=TestQuestions
        fields='__all__'
        
class TestScoreForm(ModelForm):
    class Meta:
        model=TestScore
        fields='__all__'