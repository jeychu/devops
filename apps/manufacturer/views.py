# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Manufacturer, ProductModel
from .serializers import ManufacturerSerializer, ProductModelSerializer

# Create your views here.
class ManufacturerViewset(viewsets.ModelViewSet):
    """
    retrieve: \r\nReturn the specified manufacturer's information
    list: \r\nReturn the list of all manufacturers
    update: \r\nUpdate the info of manufacturer
    destroy: \r\nDelete the info of manufacturer
    create: \r\nCreate an manufacturer entry
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductModelViewset(viewsets.ModelViewSet):
    """
    retrieve: \r\nReturn the specified productModel's information
    list: \r\nReturn the list of all productModels
    update: \r\nUpdate the info of productModel
    destroy: \r\nDelete the info of productModel
    create: \r\nCreate an productModel entry
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
