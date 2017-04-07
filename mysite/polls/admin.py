from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
		# def __init__(self, arg):
		# 	super(Question, self).__init__()
		# 	self.arg = arg
	fields = ['pub_date','question_text']

admin.site.register(Question, QuestionAdmin)