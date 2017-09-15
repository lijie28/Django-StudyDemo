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
    num = 1
    v = tools.getTheOneLoc(zArr,num)
    strv = ''
    for i in range(len(v)):
        if i ==0:
            strv = strv + zArr[i][v[i]] 
        else:
            strv = strv +'|'+ zArr[i][v[i]] 

    context = {
        'dic': v

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
    attr_details_model = []
    for a in dic.getlist('attributes'):
        attr_detail = AttributeValue.objects.filter(a_id=a)
        attr_details.append(attr_detail)
        
    countArr = tools.getCountArr(attr_details)
    count = 1
    for x in countArr:
        count = count*x

    for a in range(count):
        loc = tools.getTheOneLoc(attr_details,a)
        print '过程',a,loc,attr_details
        mlist = []
        for i in range(len(loc)):
            mlist.append(attr_details[i][loc[i]])
        attr_details_model.append(mlist)
        print '有', attr_details_model
        

    str_attr = ''
    for i in range(len(dic.getlist('attributes'))) :
        if i == 0 :
            str_attr = dic.getlist('attributes')[i]
        else:
            str_attr = str_attr + ',' + dic.getlist('attributes')[i]


    str_category = ''
    for i in range(len(dic.getlist('categorys'))) :
        if i == 0 :
            str_category = dic.getlist('categorys')[i]
        else:
            str_category = str_category + ',' + dic.getlist('categorys')[i]
        
    goods_model = Goods.objects.create(name=dic['name'],pic=dic['pic'],categorys=str_category,attributes=str_attr,describe=dic['describe'])

    context = {
        'dic': dic ,
        'goods_model' :goods_model,
        'attrs' : attr_details_model ,
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


def changeStr(dic,para):
