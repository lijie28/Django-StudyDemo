# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Attribute(models.Model):
    name = models.CharField(max_length=250)


class Attribute_value(models.Model):
    name = models.CharField(max_length=250)
    a_id = models.CharField(max_length=250,default='0')


class Category(models.Model):
    name = models.CharField(max_length=250,default='0')


class Category_value(models.Model):
    name = models.CharField(max_length=250)
    c_id = models.CharField(max_length=250,default='0')
    # def __str__(self):
    #     return self.title 


class Goods(models.Model):
    common_id = models.CharField(max_length=250, default='0')
    name = models.CharField(max_length=250)
    goods_pic = models.CharField(max_length=250)
    stock = models.CharField(max_length=250, default='99')#库存
    categorys = models.TextField(default='null')#'c_id':'c_name',
    attributes = models.TextField(default='null')

    def __str__(self):
        return self.name 

    # def get_absolute_url(self):
    #     return reverse('shop:detail', kwargs={'id': self.common_id})


class Common(models.Model):
    name = models.CharField(max_length=250)
    goods_pics = models.CharField(max_length=250)
    categorys = models.TextField(default='null')
    attributes = models.TextField(default='null')
    def_goods_id = models.CharField(max_length=250, default='0')
    goods_ids = models.CharField(max_length=250, default='0')