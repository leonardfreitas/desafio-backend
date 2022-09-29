from django.contrib import admin

from .models import Option, Question, Quiz


admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Quiz)
