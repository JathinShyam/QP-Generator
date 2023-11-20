from django import forms
from .models import Question, QuestionPaperGenerator

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
    
class QuestionPaperGeneratorForm(forms.ModelForm):
    class Meta:
        model = QuestionPaperGenerator
        fields = ['total_marks', 'distribution']

    def clean(self):
        cleaned_data = super().clean()
        total_percentage = sum(cleaned_data['distribution'].values())
        if total_percentage != 100:
            raise forms.ValidationError("The sum of percentages must be 100%.")