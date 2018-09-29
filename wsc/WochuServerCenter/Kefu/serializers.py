from rest_framework import serializers
from Kefu.models import Offlinerefundorderslog


class OfflinerefundorderslogSerializer(serializers.Serializer):
    refundlogid = serializers.IntegerField(read_only=True)
    orderid = serializers.CharField(required=False, max_length=64, blank=True, null=True)  # Field name made lowercase.
    ordersn = serializers.CharField(required=False, max_length=32, blank=True, null=True)  # Field name made lowercase.
    complaintstype = serializers.IntegerField(required=False, blank=True, null=True)  # Field name made lowercase.
    reason = serializers.IntegerField(required=False, blank=True, null=True)
    amountreceived = serializers.DecimalField(required=False, max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountrefund = serializers.DecimalField(required=False, max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundchannel = serializers.IntegerField(required=False, blank=True, null=True)  # Field name made lowercase.
    otherpartyaccount = serializers.CharField(required=False, blank=True, null=True)  # Field name made lowercase.
    refundchanneldesc = serializers.CharField(required=False, max_length=128, blank=True, null=True)  # Field name made lowercase.
    creater = serializers.CharField(required=False, max_length=64, blank=True, null=True)
    createtime = serializers.DateTimeField(required=False, blank=True, null=True)  # Field name made lowercase.

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Offlinerefundorderslog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.orderid = validated_data.get('orderid', instance.orderid)
        instance.ordersn = validated_data.get('ordersn', instance.ordersn)
        instance.complaintstype = validated_data.get('complaintstype', instance.complaintstype)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.amountreceived = validated_data.get('amountreceived', instance.amountreceived)
        instance.amountrefund = validated_data.get('amountrefund', instance.amountrefund)
        instance.refundchannel = validated_data.get('refundchannel', instance.refundchannel)
        instance.otherpartyaccount = validated_data.get('otherpartyaccount', instance.otherpartyaccount)
        instance.refundchanneldesc = validated_data.get('refundchanneldesc', instance.refundchanneldesc)
        instance.creater = validated_data.get('creater', instance.creater)
        instance.createtime = validated_data.get('createtime', instance.createtime)

        instance.save()
        return instance