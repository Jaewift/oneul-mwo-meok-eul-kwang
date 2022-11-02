from django.shortcuts import render, get_object_or_404, redirect
#from .models import Question
#from .forms import QuestionForm
from django.utils import timezone


def index(request):
    '''
    kweat 필터
    '''
    #question_list = Question.objects.order_by('-create_date')
    #context = {'question_list': question_list}
    return render(request, 'kweat_filter_search.html')