import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # 문자
    question_text = models.CharField(max_length=200)
    # 시간
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # 외래키 - question 참조 // on_delete -> question 삭제시 답변 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text