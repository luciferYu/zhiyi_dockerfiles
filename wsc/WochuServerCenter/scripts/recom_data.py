# -*- coding: utf-8 -*-
# Author: YuZhiYi
# @Time : 2018/9/25 18:27
# @File : recom_data.py
# @Site : wochu.cn
from Kefu.models import Goodsinfo,GoodsRecommendShelf
import random
import uuid

def run():
    '''制造测试数据'''
    for ginfo in Goodsinfo.objects.all()[100:200]:
        print(ginfo.name)
        print(ginfo.guid)
        grecom = GoodsRecommendShelf()
        grecom.guid = uuid.uuid1()
        grecom.goodsinfo = ginfo
        grecom.sn = ginfo.sn
        grecom.name = ginfo.name
        grecom.goodslocation =1
        grecom.goodssort = random.randint(1,998)
        grecom.save()
