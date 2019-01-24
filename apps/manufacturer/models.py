# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    vendor_name     = models.CharField("vendor_name",max_length=32, db_index=True, unique=True)
    tel             = models.CharField("telphone",null=True, max_length=15)
    mail            = models.CharField("email",null=True, max_length=32)
    remark          = models.CharField("remarks", max_length=300, null=True)

    def __str__(self):
        return self.vendor_name

    class Meta:
        db_table = "resource_manufacturer"
        ordering = ["id"]

class ProductModel(models.Model):
    model_name      = models.CharField("xinghaomingcheng", max_length=20)
    vendor          = models.ForeignKey(Manufacturer, verbose_name="suoshuzhizaoshang")

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = "resource_productmodel"
        ordering = ["id"]

