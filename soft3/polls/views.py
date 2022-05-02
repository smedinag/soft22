from django.shortcuts import render
from django.http import Http404
from django.shortcuts import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list }
    ##output = '---'.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La pregunta NO existe!")
    return render(request, 'polls/detail.html',{'question':question})
   # return HttpResponse(" Esta es la pregunta %s" % question_id)

def results(request, question_id):
    response = "Esta es la página de resultados de la pregunta %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s" % question_id)


