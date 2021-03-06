# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-22 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='changshangmingcheng')),
                ('tel', models.CharField(max_length=15, null=True, verbose_name='lianxidianhua')),
                ('mail', models.CharField(max_length=32, null=True, verbose_name='lianxiyoujian')),
                ('remark', models.CharField(max_length=300, null=True, verbose_name='beizhu')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'resource_manufacturer',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20, verbose_name='xinghaomingcheng')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturer.Manufacturer', verbose_name='suoshuzhizaoshang')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'resource_productmodel',
            },
        ),
    ]
