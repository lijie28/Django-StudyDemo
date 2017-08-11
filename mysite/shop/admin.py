# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Goods, Category

admin.site.register(Goods)
admin.site.register(Category)
