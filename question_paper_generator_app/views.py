from django.shortcuts import render, redirect
from .forms import QuestionForm, QuestionPaperGeneratorForm
from .models import Question

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

def add_question_paper_generator(request):
    if request.method == 'POST':
        form = QuestionPaperGeneratorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuestionPaperGeneratorForm()
    return render(request, 'add_question_paper_generator.html', {'form': form})