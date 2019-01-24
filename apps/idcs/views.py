# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Idc
from .serializers import IdcSerializer


class IdcViewSet(viewsets.ModelViewSet):
    """
    retrieve: \r\nReturn the specified idc's information
    list: \r\nReturn the list of all idcs
    update: \r\nUpdate the info of IDC
    destroy: \r\nDelete the info of IDC
    create: \r\nCreate an IDC entry
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer




