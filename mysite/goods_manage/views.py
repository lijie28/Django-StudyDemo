# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from shop.models import Goods, Category, Attribute, AttributeValue
from mysite import tools
# from mysite.tools import NKValue as nk
# import nk as NKValue
from django.forms.models import model_to_dict  

# Create your views here.

zArr = [["a1","a2","c2","c3"],["b1","b2","b3","b4","b5"],["c1","c2","c3","c4"]]

def debug (request):
    num = 12
    v = tools.getTheOne(zArr,num)
    strv = ''
    for i in range(len(v)):
        if i ==0:
            strv = strv + zArr[i][v[i]] 
        else:
            strv = strv +'|'+ zArr[i][v[i]] 

    context = {
        'dic': strv

    }
    return render(request, 'goodsmanage/success.html', context)
    # return h({{ v }})





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
    data_arr = dic.getlist('attributes')
    strv = ''
    # attr_details = countList(dic.getlist('attributes'))
    for i in range(len(data_arr)):
        tools.getTheOne(zArr,num)

        
        if i ==0:
            strv = strv + data_arr[i][v[i]]['value'] 
        else:
            strv = strv +'|'+ data_arr[i][v[i]]['value']
    # # for a in dic.getlist('attributes'):
    #     attr_detail = AttributeValue.objects.filter(a_id=a)
    #     attr_details.append(attr_detail)
    #     count.append (len(a))
            
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
