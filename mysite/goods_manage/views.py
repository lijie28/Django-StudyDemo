# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from shop.models import Goods, Category, Attribute, AttributeValue
from mysite import tools

from django.forms.models import model_to_dict  

# Create your views here.


def add_success(request):
    dic = tools.get_parameters(request)
    context = {
        'dic': dic ,
    }
    return render(request, 'goodsmanage/success.html', context)


def add_goods_attr(request):
    """add goods attribute
    """
    dic = tools.get_parameters(request)
    # attr = AttributeValue.objects.filter(a_id='1')

    attr_details = []
    for a in dic.getlist('attributes'):
        attr_detail = AttributeValue.objects.filter(a_id=a)
        attr_details.append(attr_detail)
        # for x in attr_detail:
        #     attr_details.append(x)
            
    context = {
        'dic': dic ,
        'attrs' : attr_details ,
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
