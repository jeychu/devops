# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.

User = get_user_model()

class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve: return the specified user's information
    list: return the list of all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
