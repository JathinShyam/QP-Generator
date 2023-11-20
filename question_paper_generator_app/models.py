from django.db import models

class Question(models.Model):
    question = models.TextField()
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    marks = models.IntegerField()

class QuestionStore(models.Model):
    questions = models.ManyToManyField(Question)

class QuestionPaperGenerator(models.Model):
    question_store = models.ForeignKey(QuestionStore, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    distribution = models.JSONField()

    def generate_question_paper(self):
        # Your code to generate the question paper goes here
        pass