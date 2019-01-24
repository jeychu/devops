# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from manufacturer.models import Manufacturer, ProductModel
from idcs.models import Idc
from cabinet.models import Cabinet


class Server(models.Model):
    """
    server model
    """
    ip              = models.CharField(max_length=15, db_index=True, unique=True, help_text="IP")
    hostname        = models.CharField(max_length=20, db_index=True, unique=True, help_text="hostname")
    cpu             = models.CharField(max_length=50, help_text="CPU")
    mem             = models.CharField(max_length=32, help_text="memory")
    disk            = models.CharField("disk", max_length=200, help_text="disk")
    os              = models.CharField("OS", max_length=50, help_text="OS")
    sn              = models.CharField("sn", max_length=50, db_index=True, help_text="SN")
    manufacturer    = models.ForeignKey(Manufacturer, verbose_name="manufacturer", help_text="manufacturer")
    model_name      = models.ForeignKey(ProductModel, verbose_name="server model", help_text="server model")
    rmt_card_ip     = models.CharField("rm_card_ip", max_length=15, db_index=True, unique=True, help_text="ip of the remote manage card")
    idc             = models.ForeignKey(Idc, null=True, verbose_name="house located in", help_text="house located in")
    cabinet         = models.ForeignKey(Cabinet, null=True, verbose_name="cabinet located in", help_text="cabinet located in")
    cabinet_position= models.CharField("the position in the cabinet", max_length=20, help_text="cabinet position")
    uuid            = models.CharField("UUID", db_index=True, unique=True,max_length=30, help_text="UUID")
    last_check      = models.DateTimeField("last_check_time", db_index=True, auto_now=True, help_text="last check time")

    def __str__(self):
        return self.ip

    class Meta:
        db_table = "resource_servers"
        ordering = ["id"]


class NetworkDevice(models.Model):
    """
    NIC model
    """
    name            = models.CharField("NIC name", max_length=20, help_text="NIC name")
    mac_address     = models.CharField("MAC_address", max_length=30, help_text="MAC address")
    host            = models.ForeignKey(Server, verbose_name="server located in", help_text="server located in")
    remark          = models.CharField("remarks", max_length=200, help_text="remarks")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "resource_network_device"
        ordering = ["id"]


class IP(models.Model):
    """
    IP model
    """
    ip_addr         = models.CharField("ip addr", max_length=15, db_index=True, unique=True, help_text="ip addr")
    netmask         = models.CharField("subnet_mask", max_length=15, help_text="netmask")
    device          = models.ForeignKey(NetworkDevice, verbose_name="NIC located in", help_text="NIC located in")
    remark          = models.CharField("remarks", max_length=200, help_text="remarks", null=True)

    def __str__(self):
        return self.ip_addr

    class Meta:
        db_table = "resource_ip"
        ordering = ["id"]

