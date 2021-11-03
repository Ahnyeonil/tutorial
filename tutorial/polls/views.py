from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
    # views 기본
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # HttpResponse, loader 추가
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # # context를 template에 데이터 전달
    # context = {
    #     'latest_question_list' : latest_question_list
    # }
    # return HttpResponse(template.render(context, request))

    # render 추가
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # detail 기본
    # return HttpResponse("You're looking at question %s." % question_id)

    #404 error 추가
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question' : question})

    #404 error shortcuts 추가
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)