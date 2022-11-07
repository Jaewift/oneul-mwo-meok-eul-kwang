from django.contrib import admin
from django.urls import path, include
from KWeat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KWeat.urls')),
]
