from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404

# Create your views here.
def index(request):
    latest_questions_list = Question.objects.order_by("pub_date")
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list":latest_questions_list,
    }
    # return HttpResponse(template.render(context=context,request=request))
    return render(request,"polls/index.html",context)

def details(request,question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/details.html",{"question":question})

def results(request, question_id):
    response = f"You are looking at the result of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")