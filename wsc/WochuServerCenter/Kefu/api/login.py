from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from Kefu.models import AuthUser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@permission_classes((AllowAny,))
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        try:
            user = AuthUser.objects.get(username=username, password=password)
        except AuthUser.DoesNotExist:
            return Response({"status": "fail", "message": "账号或密码错误！"})
        # user = AuthUser.objects.get('chengxiao')
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({"status": "ok", "data": {"token": token, "icon": "http://wmall.wochu.cn/h5/personal/img/cust-icon-nologin.png", "nickname": user.username, "id": user.pid}})

