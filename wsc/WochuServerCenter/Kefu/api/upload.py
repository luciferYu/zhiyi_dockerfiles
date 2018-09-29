import datetime
import os

import oss2
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@permission_classes((AllowAny,))
class UploadView(APIView):
    def post(self, request, *args, **kwargs):
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("img", None)
        if File is None:
            return Response("no files for upload!")
        else:
            # 打开特定的文件进行二进制的写操作;
            filepath = datetime.datetime.now().strftime("%Y%m%d%H%M%S") +os.path.splitext(File.name)[1]

            with open(filepath, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)

            auth = oss2.Auth('fUqK7apwbOAsmdpj', 'AHe9Q9JJz2FIAIcTl1BRmIn6czjQmN')
            bucket = oss2.Bucket(auth, 'oss-cn-hangzhou.aliyuncs.com', 'wochu/excel')

            result = bucket.put_object_from_file(filepath, filepath)
            return Response({"status": "ok", "data": "http://oss-cn-hangzhou.aliyuncs.com/wochu/excel/" + filepath})