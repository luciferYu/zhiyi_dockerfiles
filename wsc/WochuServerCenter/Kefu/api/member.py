import json
import datetime
from django.http import JsonResponse
from rest_framework.decorators import authentication_classes
from Kefu.models import Member
from Kefu.utils.returnResponse import returnResponse
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.serializers.pager import PagerMemberSerialiser
from Kefu.utils.MyPageHelper import MyPageNumberPagination


class MemberView(APIView):
    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        memberAccount = request.GET.get('account', '')

        member = Member.objects.all().exclude(account__endswith='deleted')
        try:
            if memberAccount != '':
                member = member.filter(account=memberAccount)
        except member.DoesNotExist:
            return Response({"status": "fail", "message": "没有此会员,请检查会员名称"})

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_member = pg.paginate_queryset(queryset=member, request=request, view=self)
        # 对数据进行序列化
        ser = PagerMemberSerialiser(instance=page_member, many=True)

        # 获取总条数
        total = member.count()

        # 获取当前页数
        page = int(request.GET.get('page', '1'))

        # 计算总页数
        yushu = total % pagesize
        pagecount = total // pagesize
        if yushu > 0:
            pagecount = pagecount + 1

        return returnResponse({"pagedata": ser.data,
                               "pageheader": {"pagecount": pagecount, "page": page, "pagesize": pagesize,
                                              "total": total}})

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def put(self, request, *args, **kwargs):
        value = json.loads(request.body)
        if value == '':
            return JsonResponse({"status": "fail", "message": "参数异常"})
        id = value.get('id')
        account = value.get('account')

        try:
            member = Member.objects.get(pid=id)
            member.account = account
            member.refreshdate = datetime.datetime.now()
            member.save()
        except Member.DoesNotExist:
            return JsonResponse({"status": "fail", "code": 404, "message": "没有找到对应数据"})
        return JsonResponse({"status": "ok", "code": 200, "message": "修改成功"})

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def delete(self, request, *args, **kwargs):
        '''
        根据会员账号删除密码  http://127.0.0.1:8000/member/delete?account=133019161151</br>
        传入参数:</br>
            会员账号(必填)</br>
            例：{"memberAccount":"13671877857"}</br>
        返回参数</br>
            {"status": "ok", "code": 200, "message": "删除成功"}</br>
        '''

        value = json.loads(request.body)
        if value == '':
            return JsonResponse({"status": "fail", "message": "参数异常"})
        memberAccount = value.get('memberAccount')
        try:
            member = Member.objects.get(account=memberAccount)
            member.account = member.account + '-' + str(int(datetime.datetime.now().timestamp())) +'-' + 'deleted'  # 在会员号后增加a来删除会员
            member.save()  # 保存修改
        except Member.DoesNotExist:
            return JsonResponse({"status": "fail", "code": 404, "message": "没有找到对应数据"})
        return JsonResponse({"status": "ok", "code": 200, "message": "删除成功"})

