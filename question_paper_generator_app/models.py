from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Question(models.Model):
    question = models.TextField()
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.subject} - {self.topic} - {self.difficulty}'

