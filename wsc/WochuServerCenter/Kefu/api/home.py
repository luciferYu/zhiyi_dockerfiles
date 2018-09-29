import time
import datetime

from django.http import JsonResponse
from rest_framework.decorators import authentication_classes
from Kefu.models import Orders
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from Kefu.utils.myauth import JSONWebTokenAuthentication


class HomeView(APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        # 今天日期
        today = datetime.date.today()

        # 昨天时间
        yesterday = today - datetime.timedelta(days=1)

        # 明天时间
        tomorrow = today + datetime.timedelta(days=1)

        # 昨天开始时间戳
        ytd_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))

        # 昨天结束时间戳
        ytd_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1

        # 今天开始时间戳
        td_start_time = ytd_end_time + 1

        # 今天结束时间戳
        td_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1

        ytdOrderNum = Orders.objects.values("createtime").filter(createtime__range=[ytd_start_time, ytd_end_time]).count()
        tdOrderNum = Orders.objects.values("createtime").filter(createtime__range=[td_start_time, td_end_time]).count()

        # 小时区间订单数
        chartGroup = Orders.objects.raw('''
            SELECT orderId, FROM_UNIXTIME( createTime, '%%H') AS time, count(1) AS orderCount from orders
            where createTime > %s
            and createTime < %s
            GROUP BY FROM_UNIXTIME(createTime, '%%Y-%%m-%%d %%H')
        ''', [ytd_start_time, td_end_time])

        # 昨日小时区间累计订单数
        ytdSumGroup = Orders.objects.raw('''
            select (
                    select count(1) from orders
                    where cast(FROM_UNIXTIME(T1.createTime) as DATE) >= cast(FROM_UNIXTIME(createTime) as DATE)
                          AND FROM_UNIXTIME(T1.createTime, '%%H') >= FROM_UNIXTIME(createTime, '%%H')
                          AND createTime> %s
                          AND createTime<%s
                    )orderNum,
                    orderId,
                   count(1) as NUM1,
                   FROM_UNIXTIME(T1.createTime, '%%H') AS time,
                   cast(FROM_UNIXTIME(createTime) as DATE) as createTime
            FROM orders T1
            WHERE T1.createTime>%s
            AND T1.createTime<%s
            GROUP BY FROM_UNIXTIME(T1.createTime, '%%H'),
                     cast(FROM_UNIXTIME(createTime) as DATE)
             order by cast(FROM_UNIXTIME(createTime) as DATE),FROM_UNIXTIME(T1.createTime, '%%H')
        ''', [ytd_start_time, ytd_end_time, ytd_start_time, ytd_end_time])

        # 今日小时区间累计订单数
        tdSumGroup = Orders.objects.raw('''
            select (
                    select count(1) from orders
                    where cast(FROM_UNIXTIME(T1.createTime) as DATE) >= cast(FROM_UNIXTIME(createTime) as DATE)
                          AND FROM_UNIXTIME(T1.createTime, '%%H') >= FROM_UNIXTIME(createTime, '%%H')
                          AND createTime> %s
                          AND createTime<%s
                    )orderNum,
                    orderId,
                   count(1) as NUM1,
                   FROM_UNIXTIME(T1.createTime, '%%H') AS time,
                   cast(FROM_UNIXTIME(createTime) as DATE) as createTime
            FROM orders T1
            WHERE T1.createTime>%s
            AND T1.createTime<%s
            GROUP BY FROM_UNIXTIME(T1.createTime, '%%H'),
                     cast(FROM_UNIXTIME(createTime) as DATE)
             order by cast(FROM_UNIXTIME(createTime) as DATE),FROM_UNIXTIME(T1.createTime, '%%H')
        ''', [td_start_time, td_end_time, td_start_time, td_end_time])

        ytdGroup = chartGroup[:24]
        tdGroup = chartGroup[24:]

        tdTimeData = list()
        ytdTimeData = list()
        tdSumTimeData = list()
        ytdSumTimeData = list()

        dateRange = list()
        for item in ytdGroup:
            dateRange.append(item.time)
            ytdTimeData.append(item.orderCount)

        for item in tdGroup:
            tdTimeData.append(item.orderCount)

        for item in ytdSumGroup:
            ytdSumTimeData.append(item.orderNum)

        for item in tdSumGroup:
            tdSumTimeData.append(item.orderNum)

        return JsonResponse({
            "status": "ok",
            "data": {
                "datetime": dateRange,
                "todayOrderNum": tdOrderNum,
                "yestodayOrderNum": ytdOrderNum,
                "chartData":  {
                    "tdTimeData": tdTimeData,
                    "ytdTimeData": ytdTimeData,
                    "tdSumTimeData": tdSumTimeData,
                    "ytdSumTimeData": ytdSumTimeData
                }
            }
        }, safe=False)