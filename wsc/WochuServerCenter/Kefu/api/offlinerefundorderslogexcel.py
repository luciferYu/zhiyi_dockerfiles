import datetime

from django.http import JsonResponse
import xlwt
import oss2
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from Kefu.models import Offlinerefundorderslog, Offlinerefundorderslogdetail, Orders, AfterSalesType, AuthUser
import logging
from braces.views import CsrfExemptMixin

from Kefu.utils.common import timeStampTOdatetime, complaintstypeFilter, aftersalestypeidFilter, orderstatusFilter, refundchannelFilter, sourceFilter, isreshipFilter, isrefundFilter, authuserFilter
from Kefu.utils.myauth import JSONWebTokenAuthentication

logger = logging.getLogger('scripts')


class OfflineRefundOrderLogExcelView(CsrfExemptMixin, APIView):

    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        ordersn = request.GET.get('s', '')
        begin = request.GET.get('begin', '')
        end = request.GET.get('end', '')
        aftersaletypeid = request.GET.get('aftersalestypeid', '')
        reason = request.GET.get('reason', '')
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
        else:
            return JsonResponse({"status": "fail", "message": "必须传入时间条件！"})

        if offlinerefundorderslog.count() <= 0:
            return JsonResponse({"status": "fail", "message": "没有找到对应数据！"})

        offlinerefundordersloglist = offlinerefundorderslog.values('refundlogid')

        offlinerefundorderslogdetail = Offlinerefundorderslogdetail.objects.filter(refundlogid__in=offlinerefundordersloglist)

        orderslist = Orders.objects.filter(ordersn__in=offlinerefundorderslog.values('ordersn'))

        authuserlist = AuthUser.objects.all()

        aftersalestypeidList = AfterSalesType.objects.filter(pid=0)

        reasonList = AfterSalesType.objects.exclude(pid=0)

        f = xlwt.Workbook()  # 创建工作簿

        '''
        创建第一个sheet:
          sheet1
        '''
        sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
        row0 = [u'订单编号', u'订单时间', u'投诉类型', u'订单状态', u'问题分类一', u'问题分类二', u'商品货号', u'商品名称', u'商品数量', u'商品交易价', u'商品实付金额', u'商品实付积分', u'实收金额', u'实收积分', u'订单金额',  u'退款金额',
                u'退款渠道', u'渠道描述', u'退款账号', u'来源', u'是否补货', u'是否退款', u'创建者', u'责任部门']

        # 生成第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i], self.set_style('Times New Roman', 220, True))

        # 生成第一列和最后一列(合并4行)

        orderindex = 1
        orderdetailcount = 1
        for order in offlinerefundorderslog:
            count = offlinerefundorderslogdetail.filter(refundlogid=order.refundlogid).count()
            if count == 0:
                return JsonResponse({"status": "fail", "message": "没有找到" + order.ordersn + "对应详情数据！"})

            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 0, 0, order.ordersn)  # 第一列
            try:
                orderinfo = orderslist.get(ordersn=order.ordersn)
            except Orders.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "没有找到" +order.ordersn+ "对应数据！"})

            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 1, 1, timeStampTOdatetime(orderinfo.createtime))
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 2, 2, complaintstypeFilter(order.complaintstype))
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 3, 3, orderstatusFilter(orderinfo.orderstatus))
            try:
                sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 4, 4, aftersalestypeidFilter(aftersalestypeidList, order.aftersaletypeid))
                sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 5, 5, aftersalestypeidFilter(reasonList, order.reason))
            except:
                return JsonResponse({"status": "fail", "message": "没有找到" + order.aftersaletypeid+','+order.reason + "对应数据！"})
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 12, 12, order.amountreceived)
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 13, 13, orderinfo.integral)
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 14, 14, orderinfo.orderamount)
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 15, 15, order.amountrefund)
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 16, 16, refundchannelFilter(order.refundchannel))
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 17, 17, order.refundchanneldesc)
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 18, 18, order.otherpartyaccount)

            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 19, 19, sourceFilter(order.source))
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 20, 20, isreshipFilter(order.isreship))
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 21, 21, isrefundFilter(order.isrefund))
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 22, 22, authuserFilter(authuserlist, order.creater))
            sheet1.write_merge(orderdetailcount, orderdetailcount + count - 1, 23, 23, order.deptsname)
            orderindex += 1
            orderdetailcount += count

        # 生成第二列
        i = 0
        for j in offlinerefundorderslogdetail:
            sheet1.write(i + 1, 6, j.goodssn)
            sheet1.write(i + 1, 7, j.goodsname)
            sheet1.write(i + 1, 8, j.cnt)
            sheet1.write(i + 1, 9, j.realprice)
            sheet1.write(i + 1, 10, j.paidsubtotal)
            sheet1.write(i + 1, 11, j.realintegral)
            i += 1

        filepath = 'excel/'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.xls'

        f.save(filepath)  # 保存文件

        auth = oss2.Auth('fUqK7apwbOAsmdpj', 'AHe9Q9JJz2FIAIcTl1BRmIn6czjQmN')
        bucket = oss2.Bucket(auth, 'oss-cn-hangzhou.aliyuncs.com', 'wochu/excel')

        result = bucket.put_object_from_file(filepath, filepath)
        print('http status: {0}'.format(result.status))
        print('request_id: {0}'.format(result.request_id))
        print('ETag: {0}'.format(result.etag))
        print('date: {0}'.format(result.headers['date']))

        return Response({"status": "ok", "data": "http://oss-cn-hangzhou.aliyuncs.com/wochu/excel/"+filepath})


    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式

        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height

        # borders= xlwt.Borders()
        # borders.left= 6
        # borders.right= 6
        # borders.top= 6
        # borders.bottom= 6

        style.font = font
        # style.borders = borders

        return style
