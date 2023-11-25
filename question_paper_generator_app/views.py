from django.shortcuts import render, redirect
from .forms import QuestionForm, QuestionPaperForm
from .models import Question
from django.http import HttpResponse, JsonResponse

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})


def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})


def question_paper_generate(request):
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST)
        if form.is_valid():

            total_marks = form.cleaned_data['total_marks']
            distribution_easy = form.cleaned_data['distribution_easy']
            distribution_medium = form.cleaned_data['distribution_medium']
            distribution_hard = form.cleaned_data['distribution_hard']
            # Calculate the number of questions for each difficulty based on the distribution
            total_easy = int(total_marks * (distribution_easy / 100))
            total_medium = int(total_marks * (distribution_medium / 100))
            total_hard = int(total_marks - total_easy*distribution_easy - total_medium*distribution_medium)
            
            # Retrieve questions from the database based on difficulty
            easy_questions = Question.objects.filter(difficulty='Easy').order_by('?')[:total_easy]
            medium_questions = Question.objects.filter(difficulty='Medium').order_by('?')[:total_medium]
            hard_questions = Question.objects.filter(difficulty='Hard').order_by('?')[:total_hard]

            # Format the data in JSON
            question_paper = {
                
                    'Easy': [q.question for q in easy_questions],
                    'Medium': [q.question for q in medium_questions],
                    'Hard': [q.question for q in hard_questions],
                
            }

            # Return JSON response
            return JsonResponse(question_paper)
            
    else:
        form = QuestionPaperForm()
    return render(request, 'question_paper_generate.html', {'form': form})