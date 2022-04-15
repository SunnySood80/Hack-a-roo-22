# ./employee/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('checkImage/', views.checkImage, name='Check_Image')
]