from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Menu
from .forms import RestaurantForm, MenuForm


def index(request):
    '''
    kweat 필터
    '''
    # question_list = Restaurant.objects.order_by('')
    # context = {'Res_name': question_list}
    return render(request, 'kweat_filter_search.html')