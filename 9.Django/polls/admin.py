from django.contrib import admin
from .models import Question, Choice
from jdatetime import GregorianToJalali

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date_jalali", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

   

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)



