# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Goods
from .models import Category

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'all_goods'

    def get_queryset(self):
        return Goods.objects.all()


class DetailView(generic.DetailView):
    model = Goods
    template_name = 'shop/detail.html'


# class GoodsCreate(CreateView):
#     model = Goods
#     fields = ['name', 'goods_pic']


# class GoodsUpdate(UpdateView):
#     model = Goods
#     fields = ['name', 'goods_pic']