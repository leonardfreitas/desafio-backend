from django.db import models

from apps.quiz.models import Question, Option


class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    option = models.ForeignKey(Option, on_delete=models.PROTECT)
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Quiz'
        ordering = ['name']

    def __str__(self):
        return self.name
