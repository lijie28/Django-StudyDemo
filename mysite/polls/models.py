from __future__ import unicode_literals
# import datatime
# from django.utils import timezone
from django.db import models

# Create your models here.


class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice (models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
