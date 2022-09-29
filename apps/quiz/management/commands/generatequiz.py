from django.core.management.base import BaseCommand

from apps.categories.models import Category
from apps.quiz.models import Option, Question, Quiz

questions_fake = [
    {
        "name": "Qual dessas linguagens de programação não é interpretada?",
        "options": [
            {"name": "Python", "is_correct": False},
            {"name": "Javascript", "is_correct": False},
            {"name": "C", "is_correct": True},
        ]
    },
    {
        "name": "Qual linguagem de programação é usada no Flutter?",
        "options": [
            {"name": "Ruby", "is_correct": False},
            {"name": "Dart", "is_correct": True},
            {"name": "Rust", "is_correct": False},
        ]
    },
    {
        "name": "Qual desses bancos de dados não utiliza SQL",
        "options": [
            {"name": "MongoDB", "is_correct": True},
            {"name": "Postgres", "is_correct": False},
            {"name": "SQLite", "is_correct": False},
        ]
    },
    {
        "name": "Qual ano foi criada a linguagem Python?",
        "options": [
            {"name": "2002", "is_correct": False},
            {"name": "1989", "is_correct": True},
            {"name": "1997", "is_correct": False},
        ]
    },
    {
        "name": "Qual dessas bibliotecas não pertencem ao mundo javascript?",
        "options": [
            {"name": "React", "is_correct": False},
            {"name": "Pandas", "is_correct": True},
            {"name": "Joi", "is_correct": False},
        ]
    },
    {
        "name": "Quem foi o criador da Linaguem C?",
        "options": [
            {"name": "Dennis Ritchie", "is_correct": True},
            {"name": "Guido van Rossum", "is_correct": False},
            {"name": "James Gosling", "is_correct": False},
        ]
    },
    {
        "name": "Qual dessas siglas não percente ao mundo da programação?",
        "options": [
            {"name": "TDD", "is_correct": False},
            {"name": "MVC", "is_correct": False},
            {"name": "GOV", "is_correct": True},
        ]
    },
    {
        "name": "Qual a empresa que mantém o Typescript?",
        "options": [
            {"name": "Microsoft", "is_correct": True},
            {"name": "Google", "is_correct": False},
            {"name": "Facebook", "is_correct": True},
        ]
    },
    {
        "name": "Qual a principal linguagem utilizada na construção do Google?",
        "options": [
            {"name": "Python", "is_correct": True},
            {"name": "Lua", "is_correct": False},
            {"name": "Ruby", "is_correct": True},
        ]
    },
    {
        "name": "Qual desses frameworks não é usado para desenvolvimento mobile?",
        "options": [
            {"name": "Flutter", "is_correct": False},
            {"name": "React Native", "is_correct": False},
            {"name": "Gin", "is_correct": True},
        ]
    },
]


class Command(BaseCommand):
    help = "Generate quiz for test"
    requires_migrations_checks = True

    def handle(self, *args, **options):

        questions = []
        for question in questions_fake:
            question_created = Question.objects.create(name=question['name'])
            for option in question['options']:
                Option.objects.create(
                    name=option["name"],
                    is_correct=option["is_correct"],
                    question=question_created
                )
            questions.append(question_created)

        category = Category.objects.create(name="Programação")
        quiz = Quiz.objects.create(
            name="Quiz Teste",
            category=category
        )
        quiz.questions.set(questions)

        self.stdout.write("Quiz test created successfully.")
