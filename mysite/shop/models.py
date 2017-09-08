# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=250,default='0')


class Attribute(models.Model):
    name = models.CharField(max_length=250,default='null')


class AttributeValue(models.Model):
    a_id = models.CharField(max_length=250,default='0')
    a_name = models.CharField(max_length=250,default='null')
    value = models.CharField(max_length=250,default='null')


class Goods(models.Model):
    # common_id = models.CharField(max_length=250, default='0')
    name = models.CharField(max_length=250,default='null')
    pic = models.CharField(max_length=250,default='null')
    # stock = models.CharField(max_length=250, default='99')#库存
    categorys = models.CharField(max_length=250,default='null')#'c_id':'c_name',
    attributes = models.CharField(max_length=250,default='null')
    describe = models.TextField(default='null')

    def __str__(self):
        return self.name 

    # def get_absolute_url(self):
    #     return reverse('shop:detail', kwargs={'id': self.common_id})
class PriceStock(models.Model):
    goods_id = models.CharField(max_length=250,default='null')
    attr_comb = models.CharField(max_length=250,default='null')#属性组合（1|170-175,2|黄）
    price = models.CharField(max_length=250,default='null')#
    stock = models.CharField(max_length=250, default='99')#库存
    attr_pic = models.CharField(max_length=250,default='null')#商品对应属性具体的图片  



# class Common(models.Model):
#     name = models.CharField(max_length=250)
#     goods_pics = models.CharField(max_length=250, default='null')
#     categorys = models.TextField(default='null')
#     attributes = models.TextField(default='null')
#     def_goods_id = models.CharField(max_length=250, default='0')
#     goods_ids = models.CharField(max_length=250, default='0')