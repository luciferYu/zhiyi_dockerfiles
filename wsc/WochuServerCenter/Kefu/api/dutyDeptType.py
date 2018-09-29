import json

from django.http import JsonResponse
from django.db import transaction
from rest_framework.decorators import authentication_classes
from Kefu.models import DutyDeptType
from Kefu.utils.returnResponse import returnResponse
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.MyPageHelper import MyPageNumberPagination

class DutyDeptTypeView(APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        pid = request.GET.get('pid', '')

        dutyDeptType = DutyDeptType.objects.all()
        if pid is '':
            dutyDeptTypelist = dutyDeptType.filter(pid=0)
        else:
            dutyDeptTypelist = dutyDeptType.filter(deptsid=pid)

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_aftersaletypeplist = pg.paginate_queryset(queryset=dutyDeptTypelist, request=request, view=self)

        list = []
        for pitem in dutyDeptTypelist:
            e = {}
            e['deptsId'] = pitem.deptsid
            e['name'] = pitem.name
            e['pid'] = pitem.pid
            e['path'] = pitem.path
            e['status'] = pitem.status
            clist = dutyDeptType.filter(pid=pitem.deptsid)
            if clist.count() > 0:
                children = []
                for item in clist:
                    c = {}
                    c['deptsId'] = item.deptsid
                    c['name'] = item.name
                    c['pid'] = item.pid
                    c['path'] = item.path
                    c['status'] = item.status
                    children.append(c)
                e['children'] = children
            list.append(e)

        # 获取总条数
        total = dutyDeptTypelist.count()

        # 获取当前页数
        page = int(request.GET.get('page', '1'))

        # 计算总页数
        yushu = total % pagesize
        pagecount = total // pagesize
        if yushu > 0:
            pagecount= pagecount + 1

        return returnResponse({"pagedata": list, "pageheader": {"pagecount": pagecount, "page": page, "pagesize": pagesize, "total": total}})


    @transaction.atomic
    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def post(self, request, *args, **kwargs):
        value = json.loads(request.body)
        if value == '':
            return JsonResponse({"status": "fail", "message": "参数异常"})

        pid = value.get('pid')
        if pid == '0':
            path = '/'
        else:
            try:
                dutyDeptType = DutyDeptType.objects.get(deptsid=pid)
                path = '/'+str(dutyDeptType.deptsid)
            except DutyDeptType.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "参数异常：未知部门！"})

        sid = transaction.savepoint()
        names = value.get('names')
        try:
            for name in names:
                item = {}
                item['pid'] = pid
                item['name'] = name
                item['path'] = path
                try:
                    dutyDeptType = DutyDeptType.objects.get(pid=pid, name=name, path=path, status=0)
                    transaction.savepoint_rollback(sid)  # 事务的回滚
                    return JsonResponse({"status": "fail", "message": "新增部门名称："+name+" 存在多次添加，不能重复添加！"})
                except DutyDeptType.DoesNotExist:
                    insert = DutyDeptType.objects.create(pid=pid, name=name, path=path, status=0)
                    insert.save()

            transaction.savepoint_commit(sid)  # 提交事务的逻辑
        except:
            transaction.savepoint_rollback(sid)  # 事务的回滚

        return JsonResponse({"status": "ok", "code": 200, "message": "新增成功"})


    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def put(self, request, *args, **kwargs):
        value = json.loads(request.body)
        if value == '':
            return JsonResponse({"status": "fail", "message": "参数异常"})
        id = int(value.get('id'))
        name = value.get('name')

        try:
            dutyDeptType = DutyDeptType.objects.get(deptsid=id)
            dutyDeptType.name = name
            dutyDeptType.save()
        except DutyDeptType.DoesNotExist:
            return JsonResponse({"status": "fail", "code": 404, "message": "没有找到对应数据"})
        return JsonResponse({"status": "ok", "code": 200, "message": "修改成功"})