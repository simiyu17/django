# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:46:53 2020

@author: simiyu
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeList.as_view()),
    path('<int:pk>/', views.EmployeeDetail.as_view()),
]