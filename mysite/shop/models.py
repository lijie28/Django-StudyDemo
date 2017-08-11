# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse





class Size(models.Model):
    title = models.CharField(max_length=250)


class Color(models.Model):
    title = models.CharField(max_length=250)


class Category(models.Model):
    title = models.CharField(max_length=250)

    # def __str__(self):
    #     return self.title 


class Goods(models.Model):
    name = models.CharField(max_length=250)
    goods_pic = models.CharField(max_length=250)
    stock = models.CharField(max_length=250, default='99')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,default='0')

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={'pk': self.pk})

