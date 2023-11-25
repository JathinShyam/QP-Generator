from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('', views.index, name='index'),
    path('add_question/', views.add_question, name='add_question'),
    path('question_paper_generate/', views.question_paper_generate, name='question_paper_generate'),
]

