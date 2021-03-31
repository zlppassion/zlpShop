# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(field_name='shop_price', help_text="最低价格",lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')
    # contains 是模糊查询 加上 i 不区分大小写
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')


    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))


    class Meta:
        model = Goods
        # fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
        # fields = ['pricemin', 'pricemax', 'name']
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']