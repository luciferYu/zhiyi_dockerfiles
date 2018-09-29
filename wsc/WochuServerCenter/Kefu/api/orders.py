from rest_framework.decorators import authentication_classes

from Kefu.models import Orders, Orderdetail
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from Kefu.utils.myauth import JSONWebTokenAuthentication


class GetOrderView(APIView):
    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        user = request.user
        ordersn = request.GET.get('ordersn')
        try:
            order = Orders.objects.get(ordersn=ordersn)
        except Orders.DoesNotExist:
            return JsonResponse({"status": "fail", "message": "没有找到对应数据！"})
        orderdetail = Orderdetail.objects.filter(orderid=order.orderid)

        jsonOrder = order.toJSON() #serializers.serialize("json",order)
        jsonOrderdetail = []
        for e in orderdetail:
            jsonOrderdetail.append(e.toJSON())

        return JsonResponse({"status": "ok", "data": {"order": jsonOrder, "orderDetail": jsonOrderdetail }}, safe=False)
