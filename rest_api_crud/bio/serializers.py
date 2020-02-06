# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:35:36 2020

@author: simiyu
"""

from rest_framework import serializers
from . import models


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        #fields = ('id', 'name', 'email', 'contact', 'created_at', 'updated_at',)
        model = models.Employee
        fields = '__all__'