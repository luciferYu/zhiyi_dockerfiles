from rest_framework.decorators import authentication_classes

from django.db import connection

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from Kefu.utils.common import transferGoodsRealTimeInfo
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.MyPageHelper import MyPageNumberPagination

import sys
import importlib
importlib.reload(sys)


class GoodsRealtimeInfoView(APIView):
    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        goodssn = request.GET.get('woc', '')

        cursor = connection.cursor()
        if goodssn == '':
            try:
                cursor.execute('''
                    select 
                        sn,
                        name,
                        group_concat(promotiontitle separator ',') AS goodsinfo 
                    from (
                        SELECT DISTINCT 
                             gi.sn,
                             gi.name,
                             concat(CASE promotionType WHEN '1' THEN '[满减]' WHEN '2' THEN '[满返]' WHEN '5' THEN '[满赠]' END ,promotionTitle) as promotiontitle,
                             FROM_UNIXTIME(gp.updatedTime) AS 更新时间,
                             gp.startTime,
                             gp.endTime
                        FROM goodspromotion AS gp
                        LEFT JOIN goodsinfo AS gi ON gi.guid = gp.goodsGuid) as T
                    group by sn,name;
                 ''')
                row = cursor.fetchall()
            except row.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "没有找到对应数据！"})

        else:
            cursor.execute('''
                select 
                    sn,
                    name,
                    group_concat(promotiontitle separator ',') AS goodsinfo 
                from (
                    SELECT DISTINCT 
                         gi.sn,
                         gi.name,
                         concat(CASE promotionType WHEN '1' THEN '[满减]' WHEN '2' THEN '[满返]' WHEN '5' THEN '[满赠]' END ,promotionTitle  ) as promotiontitle,
                         FROM_UNIXTIME(gp.updatedTime) AS 更新时间,
                         gp.startTime,
                         gp.endTime
                    FROM goodspromotion AS gp
                    LEFT JOIN goodsinfo AS gi ON gi.guid = gp.goodsGuid) as T
                WHERE T.sn = %s
                group by sn,name;
             ''', [goodssn])
            row = cursor.fetchall()

        # 关闭指针，释放内存
        cursor.close()

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_goodsrealtimeinfo = pg.paginate_queryset(queryset=list(row), request=request, view=self)

        # 对数据进行序列化
        ser = transferGoodsRealTimeInfo(page_goodsrealtimeinfo)

        # 获取总条数
        total = len(row)

        # 获取当前页数
        page = int(request.GET.get('page', 1))

        # 计算总页数
        yushu = total % pagesize
        pagecount = total // pagesize
        if yushu > 0:
            pagecount= pagecount + 1
        return Response({"status": "ok", "data": {"pagedata":ser, "pageheader": {"pagecount": pagecount, "page": page,"pagesize":pagesize,"total":total}}})
