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

    # 테스트케이스 개발 전 기본
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 테스트케이스 개발 (미래 시간으로 질문 생성)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # 외래키 - question 참조 // on_delete -> question 삭제시 답변 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
