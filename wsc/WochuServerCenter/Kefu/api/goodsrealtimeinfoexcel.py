import datetime

from django.db import connection
from django.http import JsonResponse
import xlwt
import oss2
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from braces.views import CsrfExemptMixin
from Kefu.utils.myauth import JSONWebTokenAuthentication

import sys
import importlib
importlib.reload(sys)

logger = logging.getLogger('scripts')


class GoodsRealtimeInfoExcelView(CsrfExemptMixin, APIView):
    @authentication_classes(JSONWebTokenAuthentication)
    @permission_classes((IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        goodssn = request.GET.get('woc', '')

        cursor = connection.cursor()
        if goodssn == '':
            try:
                cursor.execute('''
                    select 
                        sn,
                        name,
                        group_concat(promotiontitle separator ',') AS goodsinfo 
                    from (
                        SELECT DISTINCT 
                             gi.sn,
                             gi.name,
                             concat(CASE promotionType WHEN '1' THEN '[满减]' WHEN '2' THEN '[满返]' WHEN '5' THEN '[满赠]' END ,promotionTitle) as promotiontitle,
                             FROM_UNIXTIME(gp.updatedTime) AS 更新时间,
                             gp.startTime,
                             gp.endTime
                        FROM goodspromotion AS gp
                        LEFT JOIN goodsinfo AS gi ON gi.guid = gp.goodsGuid) as T
                    group by sn,name;
                 ''')
                row = cursor.fetchall()
            except row.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "没有找到对应数据！"})

        else:
            try:
                cursor.execute('''
                    select 
                        sn,
                        name,
                        group_concat(promotiontitle separator ',') AS goodsinfo 
                    from (
                        SELECT DISTINCT 
                             gi.sn,
                             gi.name,
                             concat(CASE promotionType WHEN '1' THEN '[满减]' WHEN '2' THEN '[满返]' WHEN '5' THEN '[满赠]' END ,promotionTitle  ) as promotiontitle,
                             FROM_UNIXTIME(gp.updatedTime) AS 更新时间,
                             gp.startTime,
                             gp.endTime
                        FROM goodspromotion AS gp
                        LEFT JOIN goodsinfo AS gi ON gi.guid = gp.goodsGuid) as T
                    WHERE T.sn = %s
                    group by sn,name;
                 ''', [goodssn])
                row = cursor.fetchall()
            except row.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "没有找到对应数据！"})

        # 关闭指针，释放内存
        cursor.close()
        f = xlwt.Workbook()  # 创建工作簿

        '''
        创建第一个sheet:
          sheet1
        '''
        sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
        row0 = [u'货号',u'名称',u'活动信息']

        # 生成第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i], self.set_style('Times New Roman', 220, True))

        # 生成第二列
        i = 0
        for j in row:
            sheet1.write(i + 1, 0, j[0])
            sheet1.write(i + 1, 1, j[1])
            sheet1.write(i + 1, 2, j[2])
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
