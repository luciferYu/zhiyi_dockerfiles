
from rest_framework.decorators import authentication_classes
from Kefu.models import Goodscategory
from Kefu.utils.returnResponse import returnResponse
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from Kefu.utils.myauth import JSONWebTokenAuthentication
from Kefu.utils.MyPageHelper import MyPageNumberPagination

class GoodsCategoryView(APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        pid = request.GET.get('pid', '')

        goodscategory = Goodscategory.objects.all()
        if pid is '':
            goodscategorylist = goodscategory.filter(parentid=0)
        else:
            goodscategorylist = goodscategory.filter(id=pid)

        pagesize = int(request.GET.get('pagesize', 10))

        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyPageNumberPagination(pagesize)
        # 获取分页的数据
        page_aftersaletypeplist = pg.paginate_queryset(queryset=goodscategorylist, request=request, view=self)

        list = []
        for pitem in goodscategorylist:
            e = {}
            e['id'] = pitem.id
            e['name'] = pitem.name
            e['path'] = pitem.path
            clist = goodscategory.filter(parentid=pitem.id)
            if clist.count() > 0:
                children = []
                for item in clist:
                    c = {}
                    c['id'] = item.id
                    c['name'] = item.name
                    c['path'] = item.path
                    children.append(c)
                e['children'] = children
            list.append(e)

        # 获取总条数
        total = goodscategorylist.count()

        # 获取当前页数
        page = int(request.GET.get('page', '1'))

        # 计算总页数
        yushu = total % pagesize
        pagecount = total // pagesize
        if yushu > 0:
            pagecount= pagecount + 1

        return returnResponse({"pagedata": list, "pageheader": {"pagecount": pagecount, "page": page, "pagesize": pagesize, "total": total}})