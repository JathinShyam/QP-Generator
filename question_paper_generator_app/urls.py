from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('', views.index, name='index'),
    path('add_question/', views.add_question, name='add_question'),
    path('add_question_paper_generator/', views.add_question_paper_generator, name='add_question_paper_generator'),
]

