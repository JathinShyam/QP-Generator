from django import forms
# from .models import Question, QuestionPaperGenerator
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
    

class QuestionPaperForm(forms.Form):

    total_marks = forms.IntegerField(min_value=1, required=True)
    distribution_easy = forms.FloatField(min_value=0, max_value=100, required=True)
    distribution_medium = forms.FloatField(min_value=0, max_value=100, required=True)
    distribution_hard = forms.FloatField(min_value=0, max_value=100, required=True)

 
