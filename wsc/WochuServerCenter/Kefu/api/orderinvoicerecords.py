from rest_framework.decorators import authentication_classes
from Kefu.models import Orderinvoicerecords, Orders
from Kefu.utils.returnResponse import returnResponse
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.serializers.pager import PagerOrderinvoicerecordsSerialiser
from Kefu.utils.MyPageHelper import MyPageNumberPagination
import json

class GetOrderinvoicerecordsView(APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        # TODO: orderinvoicerecords 此参数调整为sn
        sn = request.GET.get('orderinvoicerecords', '')
        try:
            order = Orders.objects.get(ordersn=sn)
        except Orders.DoesNotExist:
            return Response({"status": "fail", "message": "没有此订单,请检查单号"})

        try:
            orderinvoicerecords = Orderinvoicerecords.objects.filter(orderid=order.orderid)
        except Orderinvoicerecords.DoesNotExist:
            return Response({"status": "fail", "message": "发票处理中，请稍后再查"})

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_orderinvoicerecordslog = pg.paginate_queryset(queryset=orderinvoicerecords, request=request, view=self)
        # 对数据进行序列化
        ser = PagerOrderinvoicerecordsSerialiser(instance=page_orderinvoicerecordslog, many=True)

        # 获取总条数
        total = orderinvoicerecords.count()

        # 获取当前页数
        page = int(request.GET.get('page'))

        # 计算总页数
        yushu = total % pagesize
        pagecount = total // pagesize
        if yushu > 0:
            pagecount= pagecount + 1

        return returnResponse({"pagedata": ser.data, "pageheader": {"pagecount": pagecount, "page": page, "pagesize": pagesize, "total": total}})


    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def delete(self, request, *args, **kwargs):
        value = json.loads(request.body)
        orderid = value.get('orderId')
        orderinvoicerecords = Orderinvoicerecords.objects.filter(orderid=orderid).delete()

        return returnResponse()