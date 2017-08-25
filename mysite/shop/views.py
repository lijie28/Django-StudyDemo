# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

from django.template import RequestContext  
from django.http import HttpResponse
# from django.template import loader
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Goods, Common, Category, Attribute
# from .models import Category

import pickle
import json

# Create your views here.


#乱鸡巴写的取出数组也写对了卧槽
def newlist(l):
    nlist = []
    for d in l:
        for key in d :
            if key == '1':
                nlist.append (d[key])
    return nlist
        


def add_goods_get(request):
    return render_to_response('shop/addgoods.html')



def add_goods(request):
    return render_to_response('shop/addgoods.html')


def goods_detail(request, goods_id):
    goods = Goods.objects.get(id=goods_id)
    attributes = json.loads(goods.attributes)
    sizes = newlist(attributes)
    context = {
        'goods':goods,
        'attributes':attributes,
        'sizes':sizes
    }
    return render(request,'shop/detail.html',context)

# def goodsdetail(request,goods_id):
#     goods = Goods.objects.get(id=goods_id)
#     # template_name = 'shop/detail.html'
#     return render(request,'shop/detail.html',{'attributes':goods.attributes})


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'all_goods'

    def get_queryset(self):
        return Goods.objects.all()


# class DetailView(generic.DetailView):
#     model = Goods
#     template_name = 'shop/detail.html'

#     def get_attribute():
#         return json.loads(Goods.attributes);

class GoodsCreate(CreateView):
    model = Goods
    fields = ['name', 'goods_pic']


# class GoodsUpdate(UpdateView):
#     model = Goods
#     fields = ['name', 'goods_pic']