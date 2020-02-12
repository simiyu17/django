# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:48:59 2020

@author: simiyu
"""

from rest_framework import serializers
from . import models


class SampleDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SampleData
        fields = '__all__'