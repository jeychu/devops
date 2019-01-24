# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, mixins
from .models import Server, NetworkDevice, IP
from .serializers import ServerAutoReportSerializer, NetworkDeviceSerializer, IPSerializer, ServerSerializer

# Create your views here.
class ServerAutoReportViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create: \r\nCreate an server entry
    """
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer

class ServerViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve: \r\nReturn the specified server's information
    list: \r\nReturn the list of all servers
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve: \r\nReturn the specified networkdevice's information
    list: \r\nReturn the list of all networkdevices
    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class IPViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve: \r\nReturn the specified IP's information
    list: \r\nReturn the list of all IPs
    """
    queryset = IP.objects.all()
    serializer_class = IPSerializer