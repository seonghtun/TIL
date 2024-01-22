from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Question
from django.template import loader
from django.http import Http404


def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    print(lastest_question_list)
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : lastest_question_list,
    }    
    return HttpResponse(template.render(context, request))
    # 단축기능
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # context = {"latest_question_list": latest_question_list}
    # return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoseNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

    #단축
    # question = get_object_or_404(Question, pk = question_id)
    # return render(request, "polls/datial.html", {"question" : question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

