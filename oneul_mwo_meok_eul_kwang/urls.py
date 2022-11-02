from django.contrib import admin
from django.urls import path
from KWeat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter/', views.index),
]
