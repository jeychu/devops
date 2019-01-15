# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import Context, loader
import json
# Create your views here.


def index(request):
    print(request.method)
    print(request.GET)
    return HttpResponse("")


def index_template(request):
    #t = loader.get_template("test.html")
    context = {"name": "hello reboot !!!"}
    #return HttpResponse(t.render(context, request))
    return render(request, 'test.html', context)


def user_login(request):
    if request.method == "GET":
        return render(request, 'user_login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            login(request, user_obj)
            print("login successful!")
        else:
            print("login failed!")
    return HttpResponse("")

