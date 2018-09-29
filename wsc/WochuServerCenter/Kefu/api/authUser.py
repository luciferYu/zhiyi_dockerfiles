import datetime
import json

from django.http import JsonResponse
from rest_framework.decorators import authentication_classes
from Kefu.models import AuthUser
from Kefu.utils.returnResponse import returnResponse
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.serializers.pager import PagerAuthUserSerialiser
from Kefu.utils.MyPageHelper import MyPageNumberPagination


class AuthUserView(APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')

        user = AuthUser.objects.all()
        try:
            if username != '':
                user = user.filter(username=username)
        except user.DoesNotExist:
            return Response({"status": "fail", "message": "没有此用户,请检查用户名"})

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_authUser = pg.paginate_queryset(queryset=user, request=request, view=self)
        # 对数据进行序列化
        ser = PagerAuthUserSerialiser(instance=page_authUser, many=True)

        # 获取总条数
        total = user.count()

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
    def post(self, request, *args, **kwargs):
        value = json.loads(request.body)
        if value == '':
            return JsonResponse({"status": "fail", "message": "参数异常"})

        username = value.get('username')
        try:
            user = AuthUser.objects.get(username=username)
            return JsonResponse({"status": "fail", "message": "用户名重复"})
        except AuthUser.DoesNotExist:
            AuthUser.objects.create(
                password=value.get('password'),
                username=value.get('username'),
                email=value.get('email'),
                is_active=0,
                is_superuser=0,
                is_staff=0,
                date_joined=datetime.datetime.now()
            )

        return JsonResponse({"status": "ok", "code": 200, "message": "新增成功"})


    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def put(self, request, *args, **kwargs):
        value = json.loads(request.body)
        if value == '':
            return JsonResponse({"status": "fail", "message": "参数异常"})
        id = int(value.get('id'))
        password = value.get('password')

        try:
            user = AuthUser.objects.get(pid=id)
            user.password=password
            user.save()
        except AuthUser.DoesNotExist:
            return JsonResponse({"status": "fail", "code": 404, "message": "没有找到对应数据"})
        return JsonResponse({"status": "ok", "code": 200, "message": "修改成功"})