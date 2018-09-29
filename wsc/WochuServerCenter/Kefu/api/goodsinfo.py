# -*- coding: utf-8 -*-
# Author: YuZhiYi
# @Time : 2018/9/25 15:13
# @File : goodsinfo.py
# @Site : wochu.cn
from Kefu.models import Goodsinfo
from Kefu.utils.MyreturnResponse import returnResponse
from django.shortcuts import get_object_or_404
from Kefu.utils.MyAbstractViewSet import MyAbstractModelViewSet
from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.exceptions import *
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from Kefu.utils.MyFilter import GoodinfoPriceFilter


class GoodsInfoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    '''商品数据序列化器'''

    class Meta:
        model = Goodsinfo
        # fields = ('guid',
        # 'sn', 'name', 'icon','version', 'stock','catalogid', 'cost', 'price', 'mintemperature', 'maxtemperature', 'unit', 'origin1',
        # 'storagecondition', 'rankcount', 'rank', 'istip','skuname','issafebuy',)
        fields = '__all__'
        extra_kwargs = {
            'sn': {
                'required': False,
                'help_text': '序列号'
            }
        }


class GoodsInfoViewSet(MyAbstractModelViewSet):
    '''
    list:
    返回商品列表数据
    http://127.0.0.1:8000/goods?&name=佳沛小巨无霸金果超值6粒装劲爆团(团购)&fields=name,sn # 根据名称查询名称和sn号
    http://127.0.0.1:8000/goods?&fields=name,sn,price&ordering=-price #根据价格排序查名称和sn号价格
    http://127.0.0.1:8000/goods?&fields=name,sn,price&ordering=-price&page=2&page_size=5 分页查询

    retrieve:
    返回单个商品数据
    http://127.0.0.1:8000/goods/0005770a-7464-4dfa-b381-b273fda0feb7/ #根据uuid查询单件商品

    create:
    新增商品数据

    destroy:
    删除商品数据

    update:
    更新商品信息

    partial_update:
    更新商品部分信息
    '''
    queryset = Goodsinfo.objects.none()
    serializer_class = GoodsInfoSerializer

    lookup_field = 'guid'  # 查询项
    filter_fields = (
        'guid', 'sn', 'name', 'icon', 'version', 'stock', 'catalogid', 'cost', 'price', 'mintemperature',
        'maxtemperature',
        'unit', 'origin1', 'storagecondition', 'rankcount', 'rank', 'istip', 'skuname', 'issafebuy',)  # 过滤字段
    search_fields = ('name',)  # 搜索字段
    ordering = ('guid', 'sn', 'price')  #排序字段
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,GoodinfoPriceFilter)

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Goodsinfo.objects.using('read').all()
        else:
            return Goodsinfo.objects.all()

    def get_object(self):
        # todo 未能实现根据用户来区分权限
        obj = get_object_or_404(self.get_queryset(), guid=self.kwargs["guid"])  # pk=self.kwargs["pk"]
        self.check_object_permissions(self.request, obj)
        return obj

    # def retrieve(self, request, *args, **kwargs):
    #     good = self.get_object()
    #     goodser = self.serializer_class(good)
    #     return returnResponse(data=goodser.data, info="请求成功")

    # def create(self, request, *args, **kwargs):
    #     goodser = self.get_serializer(data=request.data)
    #     # 验证数据
    #     if not goodser.is_valid():
    #         return returnResponse(data=None, code=403, info=goodser.errors)
    #     obj, is_create = Goodsinfo.objects.get_or_create(**goodser.validated_data)
    #     if is_create:
    #         return returnResponse(data=goodser.data, info="保存成功")
    #     else:
    #         return returnResponse(data=None, code=500, info="记录已存在")
    #
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.count():
            raise NotFound


        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            pageinfo = {"pagination": {"count": self.paginator.page.paginator.count,
                                       "pageCount": self.paginator.page.paginator.num_pages,
                                       "size": self.paginator.get_page_size(request),
                                       "index": self.paginator.page.number}}
            return returnResponse(data=serializer.data, message="查询成功",**pageinfo)

        serializer = self.get_serializer(queryset, many=True)
        return returnResponse(data=serializer.data, message="查询成功")

    # @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated, DjangoModelPermissions])
    # def destroy(self, request, *args, **kwargs):
    #     '''自定义删除'''
    #     good = self.get_object()
    #     goodser = self.serializer_class(good)
    #     good.delete()
    #     return returnResponse(data=goodser.data, info="删除成功")