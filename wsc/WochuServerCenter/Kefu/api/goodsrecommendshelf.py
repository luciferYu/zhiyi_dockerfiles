# -*- coding: utf-8 -*-
# Author: YuZhiYi
# @Time : 2018/9/21 16:22
# @File : goodsrecommendshelf.py
# @Site : wochu.cn
import uuid
from Kefu.models import Goodsinfo, GoodsRecommendShelf
from Kefu.utils.MyreturnResponse import returnResponse
from Kefu.utils.MyAbstractViewSet import MyAbstractModelViewSet
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.exceptions import *
from drf_dynamic_fields import DynamicFieldsMixin
from django.shortcuts import get_object_or_404
from django.http import Http404


# class SimplifyGoodsInfoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
#     class Meta:
#         model = Goodsinfo
#         fields = ('price', 'icon')

class GoodsRecommendShelfSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    '''商品推荐序列化器'''

    # goodsinfo = SimplifyGoodsInfoSerializer(read_only=True)

    class Meta:
        model = GoodsRecommendShelf
        fields = '__all__'
        extra_kwargs = {
            'guid': {
                'help_text': 'guid'
            },
            'sn': {
                'help_text': '商品序列号'
            },
            'name': {
                'help_text': '商品名称'
            },
            'goodslocation': {
                'help_text': '货架展示位置'
            },
            'goodssort': {
                'help_text': '商品排序'
            },
            'goodsinfo': {
                'help_text': '商品guid'
            },
            'isdel': {
                'help_text': '是否删除'
            },

        }

class GoodsRecommendShelfViewSet(MyAbstractModelViewSet):
    '''
    list:
    返回所有商品推荐列表

    retrieve:
    返回单个商品推荐数据

    create:
    新增商品推荐数据

    destroy:
    删除商品推荐数据

    update:
    更新商品推荐信息

    partial_update:
    更新商品推荐部分信息
    '''
    serializer_class = GoodsRecommendShelfSerializer
    lookup_field = 'guid'  # 查询项
    filter_fields = ('guid', 'sn', 'name', 'goodslocation', 'goodssort', 'createdata', 'updatedata', 'isdel')
    ordering_fields = ('goodssort', 'createdata', 'updatedata')
    # ordering = ('id',)
    search_fields = ('name',)  # 搜索字段



    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return GoodsRecommendShelf.objects.using('read').all()  # 如果是查询使用只读数据库
        else:
            return GoodsRecommendShelf.objects.all()  # 其他则使用写库

    def get_object(self):
        try:
            obj = get_object_or_404(self.get_queryset(), guid=self.kwargs["guid"])  # pk=self.kwargs["pk"]
        except Http404:
            # return returnResponse(code=404, message='没有相关记录', status='fail')
            raise Http404
        else:
            self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        try:
            goodsguid = request.data.get('goodsinfo', '')
            ginfo = Goodsinfo.objects.get(guid=goodsguid)
            grecom = GoodsRecommendShelf()
            grecom.guid = uuid.uuid1()
            grecom.goodsinfo = ginfo
            grecom.sn = request.data.get('sn', '')
            grecom.name = request.data.get('name', '')
            grecom.goodslocation = request.data.get('goodslocation', 1)
            grecom.goodssort = request.data.get('goodssort', 999)
            grecom.save()
        except Exception as e:
            return returnResponse(code=500, message=str(e), status='fail')
        return returnResponse(data={'guid': grecom.guid}, code=201, message='新建商品推荐成功')

    def destroy(self, request, *args, **kwargs):
        try:
            # guid = request.data.get('guid', '')
            # current_good_recommend_shelf =  GoodsRecommendShelf.objects.get(guid=guid)
            current_good_recommend_shelf = self.get_object()
            current_good_recommend_shelf.isdel = 1
            current_good_recommend_shelf.save()
        except Http404:
            return returnResponse(code=404, message='没有相关记录', status='fail', data=None)
        else:
            return returnResponse(data={'guid': current_good_recommend_shelf.guid}, code=204, message='删除商品推荐成功')

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
        except Http404:
            return returnResponse(code=404, message='没有相关记录', status='fail', data=None)
        else:
            return returnResponse(data=serializer.data, code=200, message='查询成功')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # try:
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
            pageinfo = {"pagination": {"count": self.paginator.page.paginator.count,
                                       "pageCount": self.paginator.page.paginator.num_pages,
                                       "size": self.paginator.get_page_size(request),
                                       "index": self.paginator.page.number}}
            return returnResponse(data=serializer.data, message="查询成功", **pageinfo)

        serializer = self.get_serializer(queryset, many=True)
        return returnResponse(data=serializer.data, message="查询成功")

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
        except Http404:
            return returnResponse(code=404, message='没有相关记录', status='fail')
        except Exception as e:
            return returnResponse(code=500, message=str(e), status='fail')

        return returnResponse(data={'guid': instance.guid}, code=200, message='更新商品推荐成功')

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)