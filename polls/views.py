from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.


def index(req):
    # return HttpResponse("Hello World!")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    #! template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    #! return HttpResponse(template.render(context, req))

    return render(req, "polls/index.html", context)


def details(req, question_id):
    # return HttpResponse(f"You're looking at question {question_id}.")
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})


def results(req, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
