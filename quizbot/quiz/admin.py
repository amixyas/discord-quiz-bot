from django.contrib import admin
from . import models


@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer', 
        'is_correct', 
        'question'
        ]