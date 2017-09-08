# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from shop.models import Goods, Category, Attribute, AttributeValue
from mysite import tools

# Create your views here.


def add_goods_attr(request,goods_id):
    """add goods attribute
    """
    goods = Goods.objects.get(id=goods_id)
    c = tools.dbClassListToList(Category)
    a = tools.dbClassListToList(Attribute)
    dic = tools.get_parameters(request)
    context = {
        'c': c,
        'a': a,
        'dic': dic ,
        'goods' :goods
    }

    return render(request, 'goodsmanage/addgoods_attr.html', context)


def add_goods(request):
    c = tools.dbClassListToList(Category)
    a = tools.dbClassListToList(Attribute)
    dic = tools.get_parameters(request)
    context = {
        'c': c,
        'a': a,
        'dic': dic ,
        'goods' : '1'
    }

    return render(request, 'goodsmanage/addgoods.html', context)
