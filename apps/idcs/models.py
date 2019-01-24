# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Idc(models.Model):
    name    = models.CharField(max_length=32)
    address = models.CharField(max_length=200)
    phone   = models.CharField(max_length=15)
    email   = models.EmailField("email address of the IDC")
    letter  = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resources_idc'

