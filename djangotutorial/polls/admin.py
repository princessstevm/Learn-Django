from django.contrib import admin

# Register your models here.

from .models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    #fields = ["pub_date","question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        #("Date information", {"fields": ["pub_date"]})
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

#admin.site.register(Choice)

