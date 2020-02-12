# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:48:09 2020

@author: simiyu
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.SampleDataList.as_view()),
    path('<int:pk>/', views.SampleDataDetail.as_view()),
]