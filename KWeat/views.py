from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Menu
from .forms import RestaurantForm, MenuForm


def filter(request):
    '''
    kweat 필터
    '''
    res_object = Restaurant.objects.all()
    menu_object = Menu.objects.all()
    return render(request, 'kweat_filter_search.html', {'res_object': res_object, 'menu_object': menu_object })


def roulette(request):
    '''
    kweat 룰렛
    '''
    return render(request, 'kweat_roulette.html')


def questions(request):
    '''
    kweat 스무고개
    '''
    # question_list = Restaurant.objects.order_by('')
    # context = {'Res_name': question_list}
    return render(request, 'kweat_twenty_questions.html')