# QP-Generator


## Overview

The Question Paper Generator is a Django-based application designed to facilitate the creation of customized question papers. The primary goal is to store a diverse set of questions in a Question Store and dynamically generate question papers based on user-specified criteria such as total marks and the distribution of marks across difficulty levels.

## Key Components:

1. Question Store:

The application includes a storage system, known as the Question Store, which houses a collection of questions.
Each question in the store is characterized by attributes such as question text, subject, topic, difficulty level, and marks.


   {"What is the speed of light", "Physics", "Waves", "Easy", 5}

2. Question Paper Generation:

The Question Paper Generator is responsible for dynamically creating question papers based on user-defined parameters.
Users can specify the total marks for the paper and the desired distribution across difficulty levels (Easy, Medium, Hard).


Example Requirement: (100 marks, Difficulty, {20% Easy, 50% Medium, 30% Hard})
In this example, the system aims to generate a question paper with a total of 100 marks, allocating 20% to Easy questions, 50% to Medium questions, and 30% to Hard questions.

## Implementation:

1. Database Models:

The application uses Django models to represent questions and the Question Paper Generator.
The Question model includes fields for question text, subject, topic, difficulty, and marks.
The Question Paper Generator model includes information about the associated Question Store, total marks, and the distribution of marks.

2. User Interaction:

Users can interact with the system through a user-friendly interface to input their requirements.
The system validates and processes the user inputs to generate a customized question paper.

3. Flexibility and Scalability:

The design emphasizes modularity and extensibility to accommodate potential future requirements.
The application can easily scale to include additional attributes, such as topic distribution, allowing for diverse and comprehensive question papers.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JathinShyam/QP-Generator.git
   
2. Install project dependencies:
   ```bash
   pip install -r requirements.txt

3. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. Create a superuser(admin):
   ```bash
   python manage.py createsuperuser

5. Run the development server:
   ```bash
   python manage.py runserver

The project should now be accessible at http://localhost:8000/.

