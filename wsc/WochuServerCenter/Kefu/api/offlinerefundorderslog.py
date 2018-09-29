import datetime
import decimal
import json
import sys
from django.db import transaction
from django.http import JsonResponse
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from Kefu.models import Offlinerefundorderslog, Offlinerefundorderslogdetail, AuthUser
import logging
from braces.views import CsrfExemptMixin

from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.serializers.pager import PagerOfflinerefundorderslogSerialiser
from Kefu.utils.MyPageHelper import MyPageNumberPagination

logger = logging.getLogger('scripts')


class OfflineRefundOrderLogView(CsrfExemptMixin, APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        ordersn = request.GET.get('s', '')
        begin = request.GET.get('begin', '')
        end = request.GET.get('end', '')
        reason = request.GET.get('reason', '')
        aftersaletypeid = request.GET.get('aftersalestypeid', '')
        refundchannel = request.GET.get('refundchannel', '')
        complaintstype = request.GET.get('complaintstype', '')

        offlinerefundorderslog = Offlinerefundorderslog.objects.filter(status=0)

        if ordersn != '':
            offlinerefundorderslog = offlinerefundorderslog.filter(ordersn=ordersn).all()

        if aftersaletypeid != '':
            offlinerefundorderslog = offlinerefundorderslog.filter(aftersaletypeid=aftersaletypeid).all()

        if reason != '':
            offlinerefundorderslog = offlinerefundorderslog.filter(reason=reason).all()

        if refundchannel != '':
            offlinerefundorderslog = offlinerefundorderslog.filter(refundchannel=refundchannel).all()

        if complaintstype != '':
            offlinerefundorderslog = offlinerefundorderslog.filter(complaintstype=complaintstype).all()

        if begin != '' and end != '':
            offlinerefundorderslog = offlinerefundorderslog.filter(createtime__lt=end, createtime__gt=begin).all()

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination()
        # 获取分页的数据
        page_offlinerefundorderslog = pg.paginate_queryset(queryset=offlinerefundorderslog.order_by('createtime'), request=request, view=self)
        # 对数据进行序列化
        ser = PagerOfflinerefundorderslogSerialiser(instance=page_offlinerefundorderslog, many=True)

        # 获取总条数
        total = offlinerefundorderslog.count()

        # 获取当前页数
        page = int(request.GET.get('page'))
        pagesize = int(request.GET.get('size', 10))

        # 计算总页数
        yushu = total % pagesize
        pagecount = total // pagesize
        if yushu > 0:
            pagecount= pagecount + 1
        return Response({"status": "ok", "data": {"pagedata":ser.data, "pageheader": {"pagecount": pagecount, "page": page,"pagesize":pagesize,"total":total}}})



    @transaction.atomic
    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            value = json.loads(request.body)
            if value == "":
                logger.info('OfflineRefundOrderLogView post() 参数异常')
                return JsonResponse({"status": "fail", "message": "参数异常"})

            userid=str(user.pid)

            refund = str(value.get('isrefund', '-1'))

            sid = transaction.savepoint()

            if refund == '1':
                offlinerefundorderslog = Offlinerefundorderslog.objects.create(
                    orderid=str(value.get('orderid', '')),
                    ordersn=value.get('ordersn'),
                    complaintstype=int(value.get('complaintstype', '0')),
                    reason=int(value.get('reason', '0')),
                    amountreceived=decimal.Decimal(value.get('amountreceived', '0.00')),
                    amountrefund=decimal.Decimal(value.get('amountrefund', '0')),
                    refundchannel=value.get('refundchannel', '-1'),
                    otherpartyaccount=value.get('otherpartyaccount', '0'),
                    refundchanneldesc=value.get('refundchanneldesc', '0'),
                    aftersaletypeid=value.get('aftersaletypeid', '0'),
                    source=str(value.get('source', '0')),
                    deptsid=value.get('dutyDeptId', '0'),
                    deptsname=value.get('dutyDeptName', ''),
                    isreship=str(value.get('isreship', '-1')),
                    isrefund=str(value.get('isrefund', '-1')),
                    createtime=datetime.datetime.now(),
                    status=0,
                    creater=userid
                )
            else:
                offlinerefundorderslog = Offlinerefundorderslog.objects.create(
                    orderid=str(value.get('orderid', '')),
                    ordersn=value.get('ordersn'),
                    complaintstype=int(value.get('complaintstype', '0')),
                    reason=int(value.get('reason', '0')),
                    amountreceived=decimal.Decimal(value.get('amountreceived', '0.00')),
                    aftersaletypeid=value.get('aftersaletypeid', '0'),
                    source=str(value.get('source', '0')),
                    deptsid=value.get('dutyDeptId', '0'),
                    deptsname=value.get('dutyDeptName', ''),
                    isreship=str(value.get('isreship', '-1')),
                    isrefund=str(value.get('isrefund', '-1')),
                    result=str(value.get('result', '')),
                    description=str(value.get('description', '')),
                    imgages=str(value.get('images', '')),
                    createtime=datetime.datetime.now(),
                    status=0,
                    creater=userid
                )

            # 开启事物保护

            offlinerefundorderslog.save()

            goods_list_to_insert = list()

            for x in value.get('goods'):
                goods_list_to_insert.append(
                    Offlinerefundorderslogdetail(
                        refundlogid=offlinerefundorderslog.refundlogid,
                        goodssn=x.get('goodssn'),
                        goodsid=x.get('goodsguid'),
                        goodsname=x.get('goodsname'),
                        #amount=decimal.Decimal(x.get('amount', 0.00)),
                        cnt=int(x.get('cnt', '0')),
                        realprice=decimal.Decimal(x.get('realprice', '0.00')),
                        marketprice=decimal.Decimal(x.get('marketprice', '0.00')),
                        price=decimal.Decimal(x.get('price', '0.00')),
                        realintegral=decimal.Decimal(x.get('realintegral', '0.00')),
                        paidsubtotal=decimal.Decimal(x.get('paidsubtotal', '0.00'))
                    ))

            offlinerefundorderslogdetail = Offlinerefundorderslogdetail.objects.bulk_create(goods_list_to_insert)

            transaction.savepoint_commit(sid)  # 提交事务的逻辑
            return JsonResponse({"status": "ok", "data": "提交成功！"})
        except:
            transaction.savepoint_rollback(sid)  # 事务的回滚
            f = sys.exc_info()[2].tb_frame.f_back
            # f.f_code.co_name, f.f_lineno  # 函数名 行号
            return JsonResponse({"status": "fail", "message": f.f_code.co_name + '-' + f.f_lineno })

