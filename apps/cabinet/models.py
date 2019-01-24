# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from idcs.models import Idc

class Cabinet(models.Model):
    idc     = models.ForeignKey(Idc, verbose_name="Computer room located in")
    name    = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "resource_cabinet"
        ordering = ["id"]
