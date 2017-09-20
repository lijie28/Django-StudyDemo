# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

from django.template import RequestContext  
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt 
from .models import Goods, Category, Attribute,AttributeValue, PriceStock

# import numpy 

import pickle
import json
from mysite import tools

# Create your views here.


#乱鸡巴写的取出数组也写对了卧槽
def newlist(l):
    nlist = []
    for d in l:
        for key in d :
            if key == '1':
                nlist.append (d[key])
    return nlist


def goods_detail(request, goods_id):
    goods = Goods.objects.get(id=goods_id)
    price_stock = PriceStock.objects.filter(goods_id=goods_id)

    nexList = []
    a_list = goods.attributes.split(',')
    for x in a_list:
        av = AttributeValue.objects.filter(a_id=x)
        nexList.append(av)

    # attributes = json.loads(goods.attributes)
    # sizes = newlist(attributes)
    context = {
        'goods':goods,
        'attributes':goods.attributes,
        'price_stock':nexList
    }
    return render(request,'shop/detail.html',context)


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'all_goods'

    def get_queryset(self):
        return Goods.objects.all()


class GoodsCreate(CreateView):
    model = Goods
    fields = ['name', 'goods_pic']
