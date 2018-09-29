from rest_framework.decorators import authentication_classes

from django.db import connection

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from Kefu.utils.common import transferGoodsMonitor
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.MyPageHelper import MyPageNumberPagination


class GoodsMonitorView(APIView):
    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        goodssn = request.GET.get('woc', '')
        begin = request.GET.get('begin', '')
        end = request.GET.get('end', '')

        if begin == '' or end == '':
            return JsonResponse({"status": "fail", "message": "必须传入时间条件！"})

        beginNum = int(begin)
        endNum = int(end)

        cursor = connection.cursor()
        if goodssn == '':
            try:
                cursor.execute('''
                        select 
                           T2.goodssn,-- 货号
                           T2.goodsName, -- 商品名称
                           sum(cnt) as goodsQTY, -- 订单详情数量
                           T1.orderId,
                           T2.id
                        from orders as T1
                        INNER JOIN orderdetail as T2
                          ON T1.orderid = T2.orderid
                        WHERE T1.CreateTime 
                        BETWEEN %s
                        AND %s
                        AND T1.orderstatus != 2
                        GROUP BY T2.goodssn,
                                 T2.goodsName
                     ''', [beginNum, endNum])
                row = cursor.fetchall()
            except row.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "没有找到对应数据！"})

        else:
            cursor.execute('''
                    select 
                       T2.goodssn,-- 货号
                       T2.goodsName, -- 商品名称
                       sum(cnt) as goodsQTY, -- 订单详情数量
                       T1.orderid,
                       T2.id
                    from orders T1
                    INNER JOIN orderdetail T2
                      ON T1.orderid = T2.orderid
                    WHERE T1.CreateTime 
                    BETWEEN %s
                    AND %s
                    AND T2.goodssn = %s
                    AND T1.orderstatus != 2
                    GROUP BY T2.goodssn,
                             T2.goodsName
                 ''', [beginNum, endNum, goodssn])
            row = cursor.fetchall()

        # 关闭指针，释放内存
        cursor.close()

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_goodsmonitor = pg.paginate_queryset(queryset=list(row), request=request, view=self)

        # 对数据进行序列化
        ser = transferGoodsMonitor(page_goodsmonitor)

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
