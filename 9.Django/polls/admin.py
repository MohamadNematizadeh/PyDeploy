from django.contrib import admin
from .models import Question , Choice

admin.site.register(Choice)
admin.site.register(Question)