"""WochuServerCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url,include
from Kefu.api.orderinvoicerecords import GetOrderinvoicerecordsView
from Kefu.api.orders import GetOrderView
from Kefu.api.offlinerefundorderslog import OfflineRefundOrderLogView
from Kefu.api.login import LoginView
from Kefu.api.authUser import AuthUserView
from Kefu.api.offlinerefundorderslogexcel import OfflineRefundOrderLogExcelView
from Kefu.api.aftersalestype import AfterSaleTypeView
from Kefu.api.upload import UploadView
from Kefu.api.dutyDeptType import DutyDeptTypeView
from Kefu.api.home import HomeView
from Kefu.api.goodsmonitor import GoodsMonitorView
from Kefu.api.member import MemberView
from Kefu.api.goodscategory import GoodsCategoryView
from Kefu.api.goodsclassification import GoodsClassificationView
from Kefu.api.goodsrealtimeinfo import GoodsRealtimeInfoView
from Kefu.api.goodsrealtimeinfoexcel import GoodsRealtimeInfoExcelView
from Kefu.api.goodsrecommendshelf import GoodsRecommendShelfViewSet
from Kefu.api.goodsinfo import GoodsInfoViewSet
from Kefu.api.promotion import PromotionViewSet

from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='WochuServerCenter API DOC', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer],
                              authentication_classes=[], permission_classes=[], public=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', schema_view, name="docs"),
    path('order', GetOrderView.as_view()),
    path('offlinerefundorderlog', OfflineRefundOrderLogView.as_view()),
    path('login', LoginView.as_view()),
    path('orderinvoicerecords', GetOrderinvoicerecordsView.as_view()),
    path('offlinerefundorderslogexcel', OfflineRefundOrderLogExcelView.as_view()),
    path('authuser', AuthUserView.as_view()),
    path('aftersaletype', AfterSaleTypeView.as_view()),
    path('upload', UploadView.as_view()),
    path('dutyDeptType', DutyDeptTypeView.as_view()),
    path('home', HomeView.as_view()),
    path('member', MemberView.as_view()),
    path('goodsmonitor', GoodsMonitorView.as_view()),
    path('goodscategory', GoodsCategoryView.as_view()),
    path('goodsclassification', GoodsClassificationView.as_view()),
    path('goodsrealtimeinfo', GoodsRealtimeInfoView.as_view()),
    path('goodsrealtimeinfoexcelView', GoodsRealtimeInfoExcelView.as_view()),
    url(r'^goods$', GoodsInfoViewSet.as_view({'get': 'list'})),
    url(r'goodsrecommendshelf$', GoodsRecommendShelfViewSet.as_view({'post': 'create','get':'list'})),
    url(r'goodsrecommendshelf/(?P<guid>.+)/$', GoodsRecommendShelfViewSet.as_view({'delete': 'destroy','get':'retrieve','patch':'partial_update','put':'update'})),
    url(r'promotion$', PromotionViewSet.as_view({'post': 'create','get':'list'})),
    url(r'promotion/(?P<id>.+)/$', PromotionViewSet.as_view({'delete': 'destroy','get':'retrieve','patch':'partial_update','put':'update'})),
]
