from django.utils import timezone
from django.db import models
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    publish_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    vote = models.IntegerField(default='0')

    def __str__(self):
        return self.choice_text
