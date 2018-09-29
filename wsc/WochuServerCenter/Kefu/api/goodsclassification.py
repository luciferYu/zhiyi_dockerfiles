import json
import datetime
from django.http import JsonResponse
from rest_framework.decorators import authentication_classes
from Kefu.models import Goodsinfo
from Kefu.utils.returnResponse import returnResponse
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.serializers.pager import PagerGoodsInfoSerialiser
from Kefu.utils.MyPageHelper import MyPageNumberPagination


class GoodsClassificationView(APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        goodssn = request.GET.get('goodsSn', '')

        goodsinfo = Goodsinfo.objects.all()
        try:
            if goodssn != '':
                goodsinfo = goodsinfo.filter(sn=goodssn)
        except goodsinfo.DoesNotExist:
            return Response({"status": "fail", "message": "没有此商品"})

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_member = pg.paginate_queryset(queryset=goodsinfo, request=request, view=self)
        # 对数据进行序列化
        ser = PagerGoodsInfoSerialiser(instance=page_member, many=True)

        # 获取总条数
        total = goodsinfo.count()

        # 获取当前页数
        page = int(request.GET.get('page', '1'))

        # 计算总页数
        yushu = total % pagesize
        pagecount = total // pagesize
        if yushu > 0:
            pagecount= pagecount + 1

        return returnResponse({"pagedata": ser.data, "pageheader": {"pagecount": pagecount, "page": page, "pagesize": pagesize, "total": total}})

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def put(self, request, *args, **kwargs):
        value = json.loads(request.body)
        if value == '':
            return JsonResponse({"status": "fail", "message": "参数异常"})
        guid = value.get('guid')
        categoryid = value.get('currentCategoryid')

        try:
            goodsinfo = Goodsinfo.objects.get(guid=guid)
            goodsinfo.categoryid = categoryid
            goodsinfo.save()
        except Goodsinfo.DoesNotExist:
            return JsonResponse({"status": "fail", "code": 404, "message": "没有找到对应数据"})
        return JsonResponse({"status": "ok", "code": 200, "message": "修改成功"})