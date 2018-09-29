# -*- coding: utf-8 -*-
# Author: YuZhiYi
# @Time : 2018/9/27 15:03
# @File : promotion.py
# @Site : wochu.cn
# 使用promotion单表作为使用示例

from Kefu.models import Promotion
from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from django.shortcuts import get_object_or_404
from Kefu.utils.MyAbstractViewSet import MyAbstractModelViewSet2
from django.http import Http404
from Kefu.utils.MyreturnResponse import returnResponse

class PromotionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    '''促销序列化器'''
    class Meta:
        model = Promotion
        fields = '__all__'


class PromotionViewSet(MyAbstractModelViewSet2):
    '''
    list:
    返回所有促销

    retrieve:
    返回单个促销数据

    create:
    新增促销数据

    destroy:
    删除促销数据

    update:
    更新促销数据

    partial_update:
    更新部分促销信息
    '''
    serializer_class = PromotionSerializer
    lookup_field = 'id'  # 查询项
    filter_fields = ('id', 'name', 'type', 'description')
    ordering_fields = ('id','type')
    ordering = ('id',)
    search_fields = ('name',)  # 搜索字段

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Promotion.objects.using('read').all()  # 如果是查询使用只读数据库
        else:
            return Promotion.objects.all()  # 其他则使用写库

    def get_object(self):
        try:
            obj = get_object_or_404(self.get_queryset(), id=self.kwargs["id"])  # pk=self.kwargs["pk"]
        except Http404:
            raise Http404
        else:
            self.check_object_permissions(self.request, obj)
        return obj