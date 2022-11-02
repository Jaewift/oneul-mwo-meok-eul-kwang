from django import forms
from KWeat.models import Restaurant, Menu

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['Res_name', 'category', 'distance']
        labels = {
            'Res_name': '식당 이름',
            'category': '종류',
            'distance': '거리',
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['Menu_name', 'price']
        labels = {
            'Menu_name': '메뉴 이름',
            'price': '가격',
        }