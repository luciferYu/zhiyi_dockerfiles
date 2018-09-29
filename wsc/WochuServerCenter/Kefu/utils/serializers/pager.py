# api/utils/serializsers/pager.py

from rest_framework import serializers
from Kefu import models


class PagerOfflinerefundorderslogSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Offlinerefundorderslog
        fields = "__all__"


class PagerOrderinvoicerecordsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Orderinvoicerecords
        fields = "__all__"


class PagerAuthUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = "__all__"

class PagerMemberSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = "__all__"

class PagerGoodsInfoSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Goodsinfo
        fields = "__all__"