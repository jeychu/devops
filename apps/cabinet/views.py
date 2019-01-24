# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Cabinet
from .serializers import CabinetSerializer

# Create your views here.
class CabinetViewSet(viewsets.ModelViewSet):
    """
    retrieve: \r\nReturn the specified cabinet's information
    list: \r\nReturn the list of all cabinets
    update: \r\nUpdate the info of cabinet
    destroy: \r\nDelete the info of cabinet
    create: \r\nCreate an cabinet entry
    """
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
