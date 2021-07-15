from django.contrib import admin

from .models import Poll, Question


class PollAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'date_start',
        'date_end',
        'id',
    ]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'poll', 'type', 'id']


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
