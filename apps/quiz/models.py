from django.db import models

from apps.categories.models import Category


class Question(models.Model):
    name = models.CharField(max_length=120)
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ['name']

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=120)
    is_correct = models.BooleanField(default=False)
    # relations
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
        ordering = ['name']

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    # relations
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    questions = models.ManyToManyField(Question)
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Quiz'
        ordering = ['name']

    def __str__(self):
        return self.name
