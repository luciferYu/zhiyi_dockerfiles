# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime
import uuid
from django.db import models

from decimal import Decimal

class AuthUser(models.Model):
    pid = models.AutoField(db_column='id', primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def is_authenticated(self):
        return True

    class Meta:
        managed = False
        db_table = 'auth_user'


class Activitytemplate(models.Model):
    atid = models.AutoField(db_column='aTId', primary_key=True)  # Field name made lowercase.
    atname = models.CharField(db_column='aTName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sharetitle = models.CharField(db_column='shareTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sharecontent = models.CharField(db_column='shareContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shareicon = models.CharField(db_column='shareIcon', max_length=100, blank=True, null=True)  # Field name made lowercase.
    backgroundimage = models.CharField(db_column='backgroundImage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activitytemplate'


class Advertactivity(models.Model):
    title = models.CharField(max_length=255)
    pageimageurl = models.CharField(db_column='pageImageUrl', max_length=4000)  # Field name made lowercase.
    goodsimageurl = models.CharField(db_column='goodsImageUrl', max_length=255)  # Field name made lowercase.
    goodssn = models.CharField(max_length=60)
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    goodsname = models.CharField(max_length=600)
    goodsremark = models.CharField(max_length=600)
    marketprice = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    freeshipping = models.PositiveIntegerField(blank=True, null=True)
    paytype = models.CharField(max_length=255)
    advert = models.CharField(max_length=255, blank=True, null=True)
    enable = models.PositiveIntegerField(blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createby = models.IntegerField(blank=True, null=True)
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateby = models.IntegerField(blank=True, null=True)
    paytypeindex = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'advertactivity'


class Apilog(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    requestmessage = models.TextField(db_column='requestMessage', blank=True, null=True)  # Field name made lowercase.
    returnmessage = models.TextField(db_column='returnMessage', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apilog'


class ApilogHistory(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    requestmessage = models.TextField(db_column='requestMessage', blank=True, null=True)  # Field name made lowercase.
    returnmessage = models.TextField(db_column='returnMessage', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apilog_history'


class Appactivationdata(models.Model):
    aadid = models.AutoField(db_column='aadId', primary_key=True)  # Field name made lowercase.
    appversion = models.CharField(db_column='appVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobilebrand = models.CharField(db_column='mobileBrand', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobilemode = models.CharField(db_column='mobileMode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deviceidentificationcode = models.CharField(db_column='deviceIdentificationCode', max_length=128, blank=True, null=True)  # Field name made lowercase.
    osname = models.CharField(db_column='osName', max_length=5, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='osVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    source = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    activationtime = models.IntegerField(db_column='activationTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.CharField(max_length=100, blank=True, null=True)
    campaign = models.CharField(max_length=500, blank=True, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appactivationdata'


class Appadviertisement(models.Model):
    picurl = models.CharField(db_column='picUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appadviertisement'


class Appchannel(models.Model):
    code = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appchannel'


class Appdictionary(models.Model):
    key = models.CharField(max_length=55)
    value = models.TextField()
    type = models.IntegerField(blank=True, null=True)
    minversion = models.CharField(db_column='minVersion', max_length=255)  # Field name made lowercase.
    maxversion = models.CharField(db_column='maxVersion', max_length=255)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime')  # Field name made lowercase.
    sortindex = models.PositiveIntegerField(db_column='sortIndex')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appdictionary'


class Apperrorlog(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    methodname = models.CharField(db_column='methodName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    errorcode = models.CharField(db_column='errorCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    functionalmodule = models.CharField(db_column='functionalModule', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errorcontent = models.TextField(db_column='errorContent', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apperrorlog'


class Appfaq(models.Model):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    typeid = models.IntegerField(db_column='typeId', blank=True, null=True)  # Field name made lowercase.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.CharField(max_length=32, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appfaq'


class Appfaqtype(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appfaqtype'


class Appfeedback(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    typeid = models.IntegerField(db_column='typeId', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appfeedback'


class Appfeedbacktype(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appfeedbacktype'


class Appfreshtimelog(models.Model):
    logid = models.AutoField(db_column='logId', primary_key=True)  # Field name made lowercase.
    deviceidentificationcode = models.CharField(db_column='deviceIdentificationCode', max_length=128, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(max_length=128, blank=True, null=True)
    os = models.CharField(max_length=128, blank=True, null=True)
    androidid = models.CharField(db_column='androidId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    intime = models.IntegerField(db_column='inTime', blank=True, null=True)  # Field name made lowercase.
    outtime = models.IntegerField(db_column='outTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appfreshtimelog'


class Appgoodsshelf(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=64, blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.
    settings = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appgoodsshelf'


class Appgoodsshelfitem(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    shelfid = models.IntegerField(db_column='shelfId', blank=True, null=True)  # Field name made lowercase.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appgoodsshelfitem'


class Appgoodsshelftemplate(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    targetplatform = models.IntegerField(db_column='targetPlatform', blank=True, null=True)  # Field name made lowercase.
    createddate = models.IntegerField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appgoodsshelftemplate'


class Applocalerrorlog(models.Model):
    logid = models.AutoField(db_column='logId', primary_key=True)  # Field name made lowercase.
    errorcode = models.CharField(db_column='errorCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='errorMessage', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    callurl = models.CharField(db_column='callUrl', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    parameters = models.CharField(max_length=2000, blank=True, null=True)
    body = models.CharField(max_length=3000, blank=True, null=True)
    token = models.CharField(max_length=2000, blank=True, null=True)
    mobilemode = models.CharField(db_column='mobileMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operationsystem = models.CharField(db_column='operationSystem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='deviceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    appversion = models.CharField(db_column='appVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=128, blank=True, null=True)  # Field name made lowercase.
    source = models.IntegerField(blank=True, null=True)
    networktype = models.CharField(db_column='networkType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applocalerrorlog'


class Appnotice(models.Model):
    type = models.IntegerField()
    title = models.CharField(max_length=55)
    content = models.TextField()
    richtext = models.TextField(db_column='richText')  # Field name made lowercase. This field type is a guess.
    minversion = models.CharField(db_column='minVersion', max_length=55)  # Field name made lowercase.
    maxversion = models.CharField(db_column='maxVersion', max_length=55)  # Field name made lowercase.
    platformtypes = models.CharField(db_column='platformTypes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishedtime = models.IntegerField(db_column='publishedTime')  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.CharField(max_length=32, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appnotice'


class Appversion(models.Model):
    pid = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=15000)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appversion'


class Bankcustomeraccountinfo(models.Model):
    bcaid = models.CharField(db_column='bcaId', primary_key=True, max_length=50)  # Field name made lowercase.
    certificatetype = models.IntegerField(db_column='certificateType')  # Field name made lowercase.
    certificateno = models.CharField(db_column='certificateNo', max_length=130, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='clientName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(max_length=20, blank=True, null=True)
    banktype = models.IntegerField(db_column='bankType', blank=True, null=True)  # Field name made lowercase.
    cardtype = models.IntegerField(db_column='cardType', blank=True, null=True)  # Field name made lowercase.
    cardno = models.CharField(db_column='cardNo', max_length=130, blank=True, null=True)  # Field name made lowercase.
    validdate = models.CharField(db_column='validDate', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cvvcode = models.CharField(db_column='cvvCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cardstatus = models.IntegerField(db_column='cardStatus', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bankcustomeraccountinfo'


class BocomPaybackinfo(models.Model):
    version = models.CharField(max_length=100, blank=True, null=True)
    shoptraceno = models.CharField(db_column='shopTraceNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    posporderid = models.CharField(db_column='pospOrderId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    submittime = models.CharField(db_column='submitTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='merchantId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    merchantname = models.CharField(db_column='merchantName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardno = models.CharField(db_column='cardNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=50, blank=True, null=True)
    transamount = models.CharField(db_column='transAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalamountcurrency = models.CharField(db_column='totalAmountCurrency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transbonus = models.CharField(db_column='transBonus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deduction = models.CharField(max_length=50, blank=True, null=True)
    totalamount = models.CharField(db_column='totalAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shopbatchno = models.CharField(db_column='shopBatchNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=300, blank=True, null=True)
    returncode = models.CharField(db_column='returnCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    returnmessage = models.CharField(db_column='returnMessage', max_length=300, blank=True, null=True)  # Field name made lowercase.
    authcode = models.CharField(db_column='authCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    traceno = models.CharField(db_column='traceNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='batchNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hosttranstime = models.CharField(db_column='hostTransTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adddata = models.CharField(db_column='addData', max_length=300, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bocom_paybackinfo'


class BocomPayinfo(models.Model):
    version = models.CharField(max_length=100, blank=True, null=True)
    shoptraceno = models.CharField(db_column='shopTraceNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    submittime = models.CharField(db_column='submitTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='merchantId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=50, blank=True, null=True)
    totalamountcurrency = models.CharField(db_column='totalAmountCurrency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.CharField(db_column='totalAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adddata = models.CharField(db_column='addData', max_length=300, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bocom_payinfo'


class BocomRefundinfo(models.Model):
    ordersn = models.CharField(db_column='orderSn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    refundamount = models.CharField(db_column='refundAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    returnmessage = models.TextField(db_column='returnMessage', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bocom_refundinfo'


class CMaskPage(models.Model):
    channel = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=200)
    pic_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'c_mask_page'


class CParaDef(models.Model):
    para_id = models.AutoField(db_column='PARA_ID', primary_key=True)  # Field name made lowercase.
    para_name = models.CharField(db_column='PARA_NAME', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    para_desc = models.CharField(db_column='PARA_DESC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    para_value = models.CharField(db_column='PARA_VALUE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_para_def'


class CShowMaterialCategory(models.Model):
    pid = models.BigAutoField(db_column='id',primary_key=True)
    name = models.CharField(max_length=64)
    displayindex = models.IntegerField(db_column='displayIndex')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=255, blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    imageguid = models.CharField(db_column='imageGuid', max_length=128, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_show_material_category'


class CShowTemplate(models.Model):
    pid = models.CharField(db_column='ID', primary_key=True, max_length=40)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    template_type = models.IntegerField(db_column='TEMPLATE_TYPE', blank=True, null=True)  # Field name made lowercase.
    product_pic = models.CharField(db_column='PRODUCT_PIC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cook_time = models.IntegerField(db_column='COOK_TIME', blank=True, null=True)  # Field name made lowercase.
    diffculty_idx = models.IntegerField(db_column='DIFFCULTY_IDX', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.CharField(db_column='DISH_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_show_template'


class CShowTemplateMate(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MATERIAL_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='DOSAGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    material_type = models.IntegerField(db_column='MATERIAL_TYPE', blank=True, null=True)  # Field name made lowercase.
    src = models.IntegerField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='DISH_ID', blank=True, null=True)  # Field name made lowercase.
    template_id = models.CharField(db_column='TEMPLATE_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    parts_id = models.CharField(db_column='PARTS_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_show_template_mate'


class CShowTemplateStep(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    template_id = models.CharField(db_column='TEMPLATE_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pic = models.CharField(db_column='PIC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_show_template_step'


class Cancelorderadjustment(models.Model):
    account = models.CharField(max_length=64)
    ordersn = models.CharField(db_column='orderSn', max_length=20)  # Field name made lowercase.
    consignee = models.CharField(max_length=64, blank=True, null=True)
    ordercreatetime = models.IntegerField(db_column='orderCreateTime', blank=True, null=True)  # Field name made lowercase.
    deliverytimebegin = models.IntegerField(db_column='deliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    deliverytimeend = models.IntegerField(db_column='deliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cancelreson = models.CharField(db_column='cancelReson', max_length=512, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    approvedby = models.CharField(db_column='approvedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=512, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    approvedtime = models.IntegerField(db_column='approvedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cancelorderadjustment'


class Cart(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=50)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=60)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=120)  # Field name made lowercase.
    goodstitle = models.CharField(db_column='goodsTitle', max_length=120)  # Field name made lowercase.
    cnt = models.PositiveSmallIntegerField()
    extensioncode = models.CharField(db_column='extensionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isgift = models.PositiveIntegerField(db_column='isGift')  # Field name made lowercase.
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    tagids = models.CharField(db_column='tagIds', max_length=120, blank=True, null=True)  # Field name made lowercase.
    goodsattrids = models.CharField(db_column='goodsAttrIds', max_length=120)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64)  # Field name made lowercase.
    ischeck = models.TextField(blank=True, null=True)  # This field type is a guess.
    packageid = models.IntegerField(db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    packagegroupid = models.IntegerField(db_column='packageGroupId', blank=True, null=True)  # Field name made lowercase.
    packageindex = models.IntegerField(db_column='packageIndex', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Cartaddonitem(models.Model):
    name = models.CharField(max_length=128)
    promotionid = models.IntegerField(db_column='promotionId')  # Field name made lowercase.
    disabled = models.TextField()  # This field type is a guess.
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    creator = models.CharField(max_length=32)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updater = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartaddonitem'



class CheckoutOperationLog(models.Model):
    pretotalamount = models.DecimalField(db_column='preTotalAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prepayment = models.DecimalField(db_column='prePayment', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    preselectedvoucher = models.CharField(db_column='preSelectedVoucher', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    usedscore = models.IntegerField(db_column='usedScore', blank=True, null=True)  # Field name made lowercase.
    voucheramount = models.DecimalField(db_column='voucherAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vouchercodemoney = models.DecimalField(db_column='voucherCodeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='paymentAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='discountAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    voucher = models.CharField(max_length=100, blank=True, null=True)
    promotionids = models.CharField(db_column='promotionIds', max_length=30, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(max_length=30, blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    hascode = models.CharField(db_column='hasCode', max_length=512, blank=True, null=True)  # Field name made lowercase.
    secret = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkout_operation_log'


class CleanMemberdelete(models.Model):
    memberid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clean_memberdelete'


class Clickgoodlog(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=225, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clickgoodlog'


class CmsAccumulationNum(models.Model):
    accumulationnumid = models.AutoField(db_column='accumulationNumId', primary_key=True)  # Field name made lowercase.
    num = models.IntegerField()
    firstcreatetime = models.IntegerField(db_column='firstCreateTime')  # Field name made lowercase.
    lastupdatetime = models.IntegerField(db_column='lastUpdateTime')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_accumulation_num'


class CmsActivityBasicinfo(models.Model):
    activityid = models.AutoField(db_column='activityId', primary_key=True)  # Field name made lowercase.
    activitytype = models.IntegerField(db_column='activityType', blank=True, null=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    headimageid = models.CharField(db_column='headImageId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    activitybegin = models.DateTimeField(db_column='activityBegin', blank=True, null=True)  # Field name made lowercase.
    activityend = models.DateTimeField(db_column='activityEnd', blank=True, null=True)  # Field name made lowercase.
    stockoutrecommend = models.IntegerField(db_column='stockoutRecommend', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    activitycategory = models.IntegerField(db_column='activityCategory', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_activity_basicinfo'


class CmsActivityDeliverytime(models.Model):
    activitydelivertid = models.AutoField(db_column='activityDelivertId', primary_key=True)  # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityId', blank=True, null=True)  # Field name made lowercase.
    deliveryid = models.IntegerField(db_column='deliveryId', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_activity_deliverytime'


class CmsActivityGoods(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    activityprice = models.DecimalField(db_column='activityPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    breviaryimageid = models.CharField(db_column='breviaryImageId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    backgroundimageid = models.CharField(db_column='backgroundImageId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_activity_goods'


class CmsActivityGoodsdetail(models.Model):
    activityid = models.IntegerField(db_column='activityId', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='goodsId', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_activity_goodsdetail'


class CmsActivityLimit(models.Model):
    activityid = models.IntegerField(db_column='activityId', blank=True, null=True)  # Field name made lowercase.
    isnewguest = models.IntegerField(db_column='isNewGuest', blank=True, null=True)  # Field name made lowercase.
    totallimit = models.IntegerField(db_column='totalLimit', blank=True, null=True)  # Field name made lowercase.
    userdaylimit = models.IntegerField(db_column='userDayLimit', blank=True, null=True)  # Field name made lowercase.
    activityuserlimit = models.IntegerField(db_column='activityUserLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_activity_limit'


class CmsActivityPay(models.Model):
    activitypayid = models.AutoField(db_column='activityPayId', primary_key=True)  # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityId', blank=True, null=True)  # Field name made lowercase.
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_activity_pay'


class CmsActivityShareinfo(models.Model):
    activityid = models.IntegerField(db_column='activityId', blank=True, null=True)  # Field name made lowercase.
    sharetitle = models.CharField(db_column='shareTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sharedesicription = models.CharField(db_column='shareDesicription', max_length=555, blank=True, null=True)  # Field name made lowercase.
    shareimageid = models.CharField(db_column='shareImageId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_activity_shareinfo'


class CmsAdvertisementPosition(models.Model):
    pid = models.CharField(db_column='id',primary_key=True, max_length=64)
    adname = models.CharField(db_column='adName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imageid = models.CharField(db_column='imageId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=200, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_advertisement_position'


class CmsCycle(models.Model):
    cycleid = models.AutoField(db_column='cycleId', primary_key=True)  # Field name made lowercase.
    cycletype = models.IntegerField(db_column='cycleType')  # Field name made lowercase.
    cyclename = models.CharField(db_column='cycleName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cyclevalue = models.IntegerField(db_column='cycleValue')  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_cycle'


class CmsFloatingWindows(models.Model):
    imageid = models.CharField(db_column='imageId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=256, blank=True, null=True)
    redirecttype = models.IntegerField(db_column='redirectType', blank=True, null=True)  # Field name made lowercase.
    redirectvalue = models.CharField(db_column='redirectValue', max_length=256, blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_floating_windows'


class CmsGoodsInvoiceCategory(models.Model):
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_goods_invoice_category'


class CmsGoodsLabel(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    labelid = models.IntegerField(db_column='labelId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_goods_label'


class CmsGoodsPromotion(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    promotionid = models.IntegerField(db_column='promotionId', blank=True, null=True)  # Field name made lowercase.
    promotiontype = models.IntegerField(db_column='promotionType', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_goods_promotion'


class CmsHomepagepop(models.Model):
    homepagepopid = models.CharField(db_column='homePagePopId', primary_key=True, max_length=64)  # Field name made lowercase.
    imageid = models.CharField(db_column='imageId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pagename = models.CharField(db_column='pageName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    linkurl = models.CharField(db_column='linkUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(blank=True, null=True)
    homepagetype = models.IntegerField(db_column='homePageType', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    redirectingtype = models.IntegerField(db_column='redirectingType', blank=True, null=True)  # Field name made lowercase.
    redirectingvalue = models.CharField(db_column='redirectingValue', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_homepagepop'


class CmsImages(models.Model):
    pid = models.CharField(db_column='id',primary_key=True, max_length=64)
    imagename = models.CharField(db_column='imageName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(max_length=10, blank=True, null=True)
    imagesize = models.CharField(db_column='imageSize', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(max_length=20, blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.IntegerField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_images'


class CmsInvoiceCategory(models.Model):
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    taxclassification = models.CharField(db_column='taxClassification', max_length=128, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='taxRate', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    usepreferentialpolicy = models.IntegerField(db_column='usePreferentialPolicy', blank=True, null=True)  # Field name made lowercase.
    zerotaxmark = models.IntegerField(db_column='zeroTaxMark', blank=True, null=True)  # Field name made lowercase.
    taxspecialcontent = models.IntegerField(db_column='taxSpecialContent', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.IntegerField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_invoice_category'


class CmsLabels(models.Model):
    labelname = models.CharField(db_column='labelName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    begintime = models.IntegerField(db_column='beginTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    labelurl = models.CharField(db_column='labelUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    labeltype = models.IntegerField(db_column='labelType', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_labels'


class CmsLotteryNumchangeLog(models.Model):
    numchangeid = models.AutoField(db_column='numChangeId', primary_key=True)  # Field name made lowercase.
    redpagerrainid = models.IntegerField(db_column='redPagerRainId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    numchangetype = models.IntegerField(db_column='numChangeType', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    changefontval = models.IntegerField(db_column='changeFontVal')  # Field name made lowercase.
    changeafterval = models.IntegerField(db_column='changeAfterVal')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_lottery_numchange_log'


class CmsLotteryNumchangeLogCopy(models.Model):
    numchangeid = models.AutoField(db_column='numChangeId', primary_key=True)  # Field name made lowercase.
    redpagerrainid = models.IntegerField(db_column='redPagerRainId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    numchangetype = models.IntegerField(db_column='numChangeType', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    changefontval = models.IntegerField(db_column='changeFontVal')  # Field name made lowercase.
    changeafterval = models.IntegerField(db_column='changeAfterVal')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_lottery_numchange_log_copy'


class CmsLotteryPrize(models.Model):
    lotteryprizeid = models.AutoField(db_column='lotteryPrizeId', primary_key=True)  # Field name made lowercase.
    redpagerrainid = models.IntegerField(db_column='redPagerRainId')  # Field name made lowercase.
    couponname = models.CharField(db_column='couponName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    couponcode = models.CharField(db_column='couponCode', max_length=64)  # Field name made lowercase.
    total = models.IntegerField()
    usednum = models.IntegerField(db_column='usedNum')  # Field name made lowercase.
    probability = models.DecimalField(max_digits=18, decimal_places=4)
    isdefault = models.IntegerField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    lastupdatetime = models.IntegerField(db_column='lastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updateby = models.CharField(db_column='updateBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.
    prizepictures = models.CharField(db_column='prizePictures', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_lottery_prize'


class CmsLotteryRedpagerrain(models.Model):
    redpagerrainid = models.AutoField(db_column='redPagerRainId', primary_key=True)  # Field name made lowercase.
    titles = models.CharField(max_length=64, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    starttime = models.IntegerField(db_column='startTime')  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime')  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.
    createtime = models.BigIntegerField(db_column='createTime')  # Field name made lowercase.
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    sharescount = models.IntegerField(db_column='sharesCount')  # Field name made lowercase.
    ordergetcount = models.IntegerField(db_column='orderGetCount')  # Field name made lowercase.
    sharesgetcount = models.IntegerField(db_column='sharesGetCount')  # Field name made lowercase.
    lastupdatetime = models.IntegerField(db_column='lastUpdateTime')  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updateby = models.CharField(db_column='updateBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    imgurls = models.CharField(db_column='imgUrls', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    systemcount = models.IntegerField(db_column='systemCount', blank=True, null=True)  # Field name made lowercase.
    sharestitle = models.CharField(db_column='sharesTitle', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sharescontent = models.CharField(db_column='sharesContent', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sharespic = models.CharField(db_column='sharesPic', max_length=512, blank=True, null=True)  # Field name made lowercase.
    sharesinfo = models.CharField(db_column='sharesInfo', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_lottery_redpagerrain'


class CmsLotteryUserCount(models.Model):
    lotteryusercountid = models.AutoField(db_column='lotteryUserCountId', primary_key=True)  # Field name made lowercase.
    redpagerrainid = models.IntegerField(db_column='redPagerRainId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    systemcount = models.IntegerField(db_column='systemCount', blank=True, null=True)  # Field name made lowercase.
    ordercount = models.IntegerField(db_column='orderCount', blank=True, null=True)  # Field name made lowercase.
    sharescount = models.IntegerField(db_column='sharesCount', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    lastorderupatetime = models.IntegerField(db_column='lastOrderUpateTime', blank=True, null=True)  # Field name made lowercase.
    lastsharesupdatetime = models.IntegerField(db_column='lastSharesUpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_lottery_user_count'


class CmsLotteryUserCountCopy(models.Model):
    lotteryusercountid = models.AutoField(db_column='lotteryUserCountId', primary_key=True)  # Field name made lowercase.
    redpagerrainid = models.IntegerField(db_column='redPagerRainId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    systemcount = models.IntegerField(db_column='systemCount', blank=True, null=True)  # Field name made lowercase.
    ordercount = models.IntegerField(db_column='orderCount', blank=True, null=True)  # Field name made lowercase.
    sharescount = models.IntegerField(db_column='sharesCount', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    lastorderupatetime = models.IntegerField(db_column='lastOrderUpateTime', blank=True, null=True)  # Field name made lowercase.
    lastsharesupdatetime = models.IntegerField(db_column='lastSharesUpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_lottery_user_count_copy'


class CmsLotteryUserLog(models.Model):
    lotteryuserlogid = models.AutoField(db_column='lotteryUserLogId', primary_key=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    couponname = models.CharField(db_column='couponName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    couponcode = models.CharField(db_column='couponCode', max_length=64)  # Field name made lowercase.
    redpagerrainid = models.IntegerField(db_column='redPagerRainId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_lottery_user_log'


class CmsMedias(models.Model):
    mediaid = models.CharField(db_column='mediaId', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mediaurl = models.CharField(db_column='mediaUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(blank=True, null=True)
    activitytype = models.IntegerField(db_column='activityType', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_medias'


class CmsPaymentManagement(models.Model):
    channel = models.CharField(max_length=64, blank=True, null=True)
    paytypeid = models.IntegerField(db_column='payTypeId', blank=True, null=True)  # Field name made lowercase.
    paytypename = models.CharField(db_column='payTypeName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1024, blank=True, null=True)
    isdefault = models.IntegerField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_payment_management'


class CmsRechargeCoupon(models.Model):
    pid = models.CharField(db_column='id',primary_key=True, max_length=64)
    rid = models.CharField(db_column='rId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    couponid = models.IntegerField(db_column='couponId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=256, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    displayname = models.CharField(db_column='displayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    suguid = models.CharField(db_column='suGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    suname = models.CharField(db_column='suName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_recharge_coupon'


class CmsRechargeGuideline(models.Model):
    content = models.TextField(blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_recharge_guideline'


class CmsRechargeManagement(models.Model):
    pid = models.CharField(db_column='id',primary_key=True, max_length=64)
    suguid = models.CharField(db_column='suGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(blank=True, null=True)
    displayamount = models.CharField(db_column='displayAmount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.IntegerField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rechargediscountid = models.IntegerField(db_column='rechargeDiscountId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_recharge_management'


class CmsSignBonusRules(models.Model):
    signbonusrulesid = models.AutoField(db_column='signBonusRulesId', primary_key=True)  # Field name made lowercase.
    signrewardid = models.IntegerField(db_column='signRewardId')  # Field name made lowercase.
    signrulesid = models.IntegerField(db_column='signRulesId')  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_sign_bonus_rules'


class CmsSignBonusRulesAt(models.Model):
    signbonusrulesatid = models.AutoField(db_column='signBonusRulesAtId', primary_key=True)  # Field name made lowercase.
    cycleid = models.IntegerField(db_column='cycleId')  # Field name made lowercase.
    signrewardid = models.IntegerField(db_column='signRewardId')  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_sign_bonus_rules_at'


class CmsSignLog(models.Model):
    signlogid = models.AutoField(db_column='signLogId', primary_key=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    signdate = models.CharField(db_column='signDate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_sign_log'


class CmsSignReward(models.Model):
    signrewardid = models.AutoField(db_column='signRewardId', primary_key=True)  # Field name made lowercase.
    signrewardtype = models.IntegerField(db_column='signRewardType')  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)
    bussinessvalue = models.CharField(db_column='bussinessValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    num = models.IntegerField()
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_sign_reward'


class CmsSignRewardLog(models.Model):
    signrewardlogid = models.AutoField(db_column='signRewardLogId', primary_key=True)  # Field name made lowercase.
    signlogid = models.CharField(db_column='signLogId', max_length=64)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)
    createtime = models.TextField(db_column='createTime')  # Field name made lowercase.
    bussinessvalue = models.CharField(db_column='bussinessValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    num = models.IntegerField()
    signrewardtype = models.IntegerField(db_column='signRewardType')  # Field name made lowercase.
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_sign_reward_log'


class CmsSignRules(models.Model):
    signrulesid = models.AutoField(db_column='signRulesId', primary_key=True)  # Field name made lowercase.
    signrulesdays = models.IntegerField(db_column='signRulesDays')  # Field name made lowercase.
    signrulesnum = models.IntegerField(db_column='signRulesNum')  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_sign_rules'


class CmsSignRulesActivity(models.Model):
    signrulescontentid = models.AutoField(db_column='signRulesContentId', primary_key=True)  # Field name made lowercase.
    contents = models.TextField(blank=True, null=True)
    starttime = models.IntegerField(db_column='startTime')  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime')  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_sign_rules_activity'


class CmsSysuser(models.Model):
    username = models.CharField(db_column='userName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='passwordHash', max_length=128, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='displayName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_sysuser'


class CmsVoucherBatch(models.Model):
    prefix = models.CharField(max_length=32)
    startidentifier = models.IntegerField(db_column='startIdentifier')  # Field name made lowercase.
    templateid = models.IntegerField(db_column='templateId')  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime')  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime')  # Field name made lowercase.
    activedtime = models.IntegerField(db_column='activedTime')  # Field name made lowercase.
    enabled = models.IntegerField()
    description = models.CharField(max_length=128, blank=True, null=True)
    filepath = models.CharField(db_column='filePath', max_length=256)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    resultnote = models.CharField(db_column='resultNote', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_voucher_batch'


class CmsVoucherBatchItem(models.Model):
    account = models.CharField(max_length=64)
    batchid = models.IntegerField(db_column='batchId')  # Field name made lowercase.
    vouchersn = models.CharField(db_column='voucherSn', max_length=64)  # Field name made lowercase.
    status = models.IntegerField()
    description = models.CharField(max_length=128, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_voucher_batch_item'


class Cookactivity(models.Model):
    userno = models.CharField(db_column='userNo', max_length=10)  # Field name made lowercase.
    wechatnickname = models.CharField(db_column='weChatNickName', max_length=50)  # Field name made lowercase.
    dishname = models.CharField(db_column='dishName', max_length=255)  # Field name made lowercase.
    dishurl = models.CharField(db_column='dishUrl', max_length=255)  # Field name made lowercase.
    votecount = models.PositiveIntegerField(db_column='voteCount', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cookactivity'


class Cookactivityvotes(models.Model):
    caid = models.IntegerField(db_column='caId', blank=True, null=True)  # Field name made lowercase.
    openid = models.CharField(db_column='openId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cookactivityvotes'


class Countryregion(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
    path = models.CharField(max_length=64)
    pathname = models.CharField(db_column='pathName', max_length=64)  # Field name made lowercase.
    depth = models.IntegerField()
    isdirectshipping = models.IntegerField(db_column='isDirectShipping', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countryregion'


class DActCategory(models.Model):
    cate_id = models.IntegerField(db_column='CATE_ID', primary_key=True)  # Field name made lowercase.
    cate_name = models.CharField(db_column='CATE_NAME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_act_category'


class DActPartSts(models.Model):
    pid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status_name = models.CharField(db_column='STATUS_NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_act_part_sts'


class DActStatus(models.Model):
    pid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status_name = models.CharField(db_column='STATUS_NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_act_status'


class DCommentsStatus(models.Model):
    comments_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_comments_status'


class DDifficultLevel(models.Model):
    level = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_difficult_level'


class DMaterialType(models.Model):
    pid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_material_type'


class DNutritionItem(models.Model):
    pid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_nutrition_item'


class DPavStatus(models.Model):
    pid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status_name = models.CharField(db_column='STATUS_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_pav_status'


class DPicType(models.Model):
    pid = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_pic_type'


class DShowCookTime(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    time = models.CharField(db_column='TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_show_cook_time'


class DShowDifficulty(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_show_difficulty'


class DShowStatus(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    show_status = models.CharField(db_column='SHOW_STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_show_status'


class DShowTemplateType(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_show_template_type'


class DWxGroup(models.Model):
    group_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_wx_group'


class Deliverpromocode(models.Model):
    promocode = models.CharField(db_column='promoCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deliverpromocode'


class DeliveryPowerSetting(models.Model):
    deliverytimebegin = models.IntegerField(db_column='deliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    deliverytimeend = models.IntegerField(db_column='deliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    deliverytime = models.CharField(db_column='deliveryTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deliverypower = models.IntegerField(db_column='deliveryPower', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_power_setting'


class Deliveryinfoadjustment(models.Model):
    ordersn = models.CharField(db_column='orderSn', max_length=64, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(max_length=64, blank=True, null=True)
    consignee = models.CharField(max_length=64, blank=True, null=True)
    ordercreatetime = models.CharField(db_column='orderCreateTime', max_length=64, blank=True, null=True)  # Field name made lowercase.
    originaldeliverytimebegin = models.IntegerField(db_column='originalDeliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    originaldeliverytimeend = models.IntegerField(db_column='originalDeliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    deliverytimebegin = models.IntegerField(db_column='deliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    deliverytimeend = models.IntegerField(db_column='deliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    originalregion = models.CharField(db_column='originalRegion', max_length=32, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=32, blank=True, null=True)
    originaladdress = models.CharField(db_column='originalAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=128, blank=True, null=True)
    changereson = models.CharField(db_column='changeReson', max_length=512, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    approvedby = models.CharField(db_column='approvedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=512, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    approvedtime = models.IntegerField(db_column='approvedTime', blank=True, null=True)  # Field name made lowercase.
    originalmobile = models.CharField(db_column='originalMobile', max_length=16, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(max_length=16, blank=True, null=True)
    originalconsignee = models.CharField(db_column='originalConsignee', max_length=64, blank=True, null=True)  # Field name made lowercase.
    originaleventtype = models.IntegerField(db_column='originalEventType', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.IntegerField(db_column='eventType', blank=True, null=True)  # Field name made lowercase.
    originallongitude = models.DecimalField(db_column='originalLongitude', max_digits=20, decimal_places=17, blank=True, null=True)  # Field name made lowercase.
    originallatitude = models.DecimalField(db_column='originalLatitude', max_digits=20, decimal_places=17, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    streetnumber = models.CharField(db_column='streetNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    originalstreetnumber = models.CharField(db_column='originalStreetNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deliveryinfoadjustment'


class Deliverytime(models.Model):
    starthour = models.IntegerField(db_column='startHour')  # Field name made lowercase.
    startminute = models.IntegerField(db_column='startMinute')  # Field name made lowercase.
    endhour = models.IntegerField(db_column='endHour')  # Field name made lowercase.
    endminute = models.IntegerField(db_column='endMinute')  # Field name made lowercase.
    activestarthour = models.IntegerField(db_column='activeStartHour')  # Field name made lowercase.
    activestartminute = models.IntegerField(db_column='activeStartMinute')  # Field name made lowercase.
    activeendhour = models.IntegerField(db_column='activeEndHour')  # Field name made lowercase.
    activeendminute = models.IntegerField(db_column='activeEndMinute')  # Field name made lowercase.
    enabled = models.TextField()  # This field type is a guess.
    issameday = models.TextField(db_column='isSameDay')  # Field name made lowercase. This field type is a guess.
    ordercount = models.IntegerField(db_column='orderCount', blank=True, null=True)  # Field name made lowercase.
    deliverypower = models.IntegerField(db_column='deliveryPower', blank=True, null=True)  # Field name made lowercase.
    deliverytime = models.CharField(db_column='deliveryTime', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deliverytime'


class Designatedvalue(models.Model):
    maxidofpackageindex = models.IntegerField(db_column='maxIdOfPackageIndex', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'designatedvalue'


class DituiinvitationcodeBack(models.Model):
    invitationcode = models.CharField(max_length=128)
    type = models.IntegerField(blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dituiinvitationcode_back'


class ErpSaleDownStock(models.Model):
    pid = models.CharField(db_column='id',primary_key=True, max_length=64)
    goods_sn = models.CharField(max_length=20, blank=True, null=True)
    batch_no = models.CharField(max_length=20, blank=True, null=True)
    real_stock = models.IntegerField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    erp_update_date = models.DateTimeField(blank=True, null=True)
    import_date = models.DateTimeField(blank=True, null=True)
    stock_memo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'erp_sale_down_stock'


class Exchangecard(models.Model):
    code = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    shippingids = models.CharField(db_column='shippingIds', max_length=64, blank=True, null=True)  # Field name made lowercase.
    countryregionids = models.CharField(db_column='countryRegionIds', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    enabletime = models.IntegerField(db_column='enableTime', blank=True, null=True)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.
    deadlinetime = models.IntegerField(db_column='deadlineTime', blank=True, null=True)  # Field name made lowercase.
    isused = models.IntegerField(db_column='isUsed', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(blank=True, null=True)
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecard'


class ExchangecardCopy(models.Model):
    code = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    shippingids = models.CharField(db_column='shippingIds', max_length=64, blank=True, null=True)  # Field name made lowercase.
    countryregionids = models.CharField(db_column='countryRegionIds', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    enabletime = models.IntegerField(db_column='enableTime', blank=True, null=True)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.
    deadlinetime = models.IntegerField(db_column='deadlineTime', blank=True, null=True)  # Field name made lowercase.
    isused = models.IntegerField(db_column='isUsed', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(blank=True, null=True)
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecard_copy'


class ExchangecardCountryregion(models.Model):
    cardtemplateid = models.IntegerField(db_column='cardTemplateId', blank=True, null=True)  # Field name made lowercase.
    countryregionid = models.IntegerField(db_column='countryregionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecard_countryregion'


class ExchangecardShipping(models.Model):
    cardtemplateid = models.IntegerField(db_column='cardTemplateId', blank=True, null=True)  # Field name made lowercase.
    shippingid = models.IntegerField(db_column='shippingId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecard_shipping'


class Exchangecardbatchinfo(models.Model):
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(blank=True, null=True)
    channel = models.CharField(max_length=64, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    isdowload = models.IntegerField(db_column='isDowload', blank=True, null=True)  # Field name made lowercase.
    generatetime = models.IntegerField(db_column='generateTime', blank=True, null=True)  # Field name made lowercase.
    generator = models.CharField(max_length=64, blank=True, null=True)
    receiver = models.CharField(max_length=64, blank=True, null=True)
    receivetime = models.IntegerField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecardbatchinfo'


class Exchangecardcheck(models.Model):
    cardno = models.CharField(db_column='cardNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    errornum = models.IntegerField(db_column='errorNum', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.IntegerField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecardcheck'


class ExchangecardcheckCopy(models.Model):
    cardno = models.CharField(db_column='cardNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    errornum = models.IntegerField(db_column='errorNum', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.IntegerField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecardcheck_copy'


class Exchangecardtemplate(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    enabletime = models.IntegerField(db_column='enableTime', blank=True, null=True)  # Field name made lowercase.
    deadlinetime = models.IntegerField(db_column='deadlineTime', blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=64, blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(blank=True, null=True)
    creator = models.CharField(max_length=64, blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updater = models.CharField(max_length=64, blank=True, null=True)
    updatetime = models.IntegerField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    generatecount = models.IntegerField(db_column='generateCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangecardtemplate'


class Fixedtwodimensionchangedlog(models.Model):
    changeid = models.AutoField(db_column='changeId', primary_key=True)  # Field name made lowercase.
    originalredirecturl = models.CharField(db_column='originalRedirectUrl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    newredirecturl = models.CharField(db_column='newRedirectUrl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    changedtime = models.IntegerField(db_column='changedTime', blank=True, null=True)  # Field name made lowercase.
    changeuserid = models.CharField(db_column='changeUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dimensionid = models.IntegerField(db_column='dimensionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fixedtwodimensionchangedlog'


class Fixedtwodimensioncode(models.Model):
    dimensionid = models.AutoField(db_column='dimensionId', primary_key=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    generateurl = models.CharField(db_column='generateUrl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    redirecturl = models.CharField(db_column='redirectUrl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=500, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.IntegerField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fixedtwodimensioncode'


class Fixedtwodimensioncodeaccesslog(models.Model):
    accessid = models.AutoField(db_column='accessId', primary_key=True)  # Field name made lowercase.
    accesstime = models.IntegerField(db_column='accessTime', blank=True, null=True)  # Field name made lowercase.
    generateurl = models.CharField(db_column='generateUrl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    redirecturl = models.CharField(db_column='redirectUrl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dimensionid = models.IntegerField(db_column='dimensionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fixedtwodimensioncodeaccesslog'


class Gift(models.Model):
    giftid = models.AutoField(db_column='giftId', primary_key=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    activitydesc = models.CharField(db_column='activityDesc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vouchertemplateid = models.CharField(db_column='voucherTemplateId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    startday = models.CharField(db_column='startDay', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activitydesc2 = models.CharField(db_column='activityDesc2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    smscontent = models.CharField(db_column='SMScontent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gift'


class Giftdetail(models.Model):
    giftdetailid = models.AutoField(db_column='giftDetailId', primary_key=True)  # Field name made lowercase.
    giftid = models.IntegerField(db_column='giftId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=512, blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(blank=True, null=True)
    displayseq = models.IntegerField(db_column='displaySeq', blank=True, null=True)  # Field name made lowercase.
    giftname = models.CharField(db_column='giftName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'giftdetail'


class Giftshare(models.Model):
    giftshareid = models.AutoField(db_column='giftShareId', primary_key=True)  # Field name made lowercase.
    launchuserid = models.CharField(db_column='launchUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    launchtime = models.DateTimeField(db_column='launchTime', blank=True, null=True)  # Field name made lowercase.
    giftid = models.IntegerField(db_column='giftId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'giftshare'


class Giftvoucher(models.Model):
    giftvoucherid = models.AutoField(db_column='giftVoucherId', primary_key=True)  # Field name made lowercase.
    giftdetailid = models.IntegerField(db_column='giftDetailId', blank=True, null=True)  # Field name made lowercase.
    vouchertemplateid = models.IntegerField(db_column='voucherTemplateId', blank=True, null=True)  # Field name made lowercase.
    startday = models.IntegerField(db_column='startDay', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'giftvoucher'


class Goodsassociation(models.Model):
    activegoodsguid = models.CharField(db_column='activeGoodsGuid', max_length=64)  # Field name made lowercase.
    passivegoodsguid = models.CharField(db_column='passiveGoodsGuid', max_length=64)  # Field name made lowercase.
    bidirectional = models.TextField()  # This field type is a guess.
    planid = models.IntegerField(db_column='planId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsassociation'


class Goodsattribute(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    code = models.CharField(max_length=256, blank=True, null=True)
    value = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    readonly = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goodsattribute'


class Goodsbindplatform(models.Model):
    goodssn = models.CharField(db_column='goodsSn', max_length=20)  # Field name made lowercase.
    platformtype = models.IntegerField(db_column='platformType')  # Field name made lowercase.
    shopid = models.CharField(db_column='shopId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    consumerkey = models.CharField(db_column='consumerKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    goodscode = models.CharField(db_column='goodsCode', max_length=20)  # Field name made lowercase.
    goodssku = models.CharField(db_column='goodsSku', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=200, blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    updatetime = models.IntegerField(db_column='updateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsbindplatform'


class Goodsbrand(models.Model):
    name = models.CharField(max_length=64)
    displayindex = models.IntegerField(db_column='displayIndex')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsbrand'


class Goodscatalog(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodscatalog'


class Goodscategory(models.Model):
    name = models.CharField(max_length=64)
    displayindex = models.IntegerField(db_column='displayIndex')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodscategory'


class Goodscategory20170425(models.Model):
    name = models.CharField(max_length=64)
    displayindex = models.IntegerField(db_column='displayIndex')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodscategory_20170425'


class Goodscategorygallery(models.Model):
    categoryid = models.IntegerField(db_column='categoryId', primary_key=True)  # Field name made lowercase.
    imageguid = models.CharField(db_column='imageGuid', max_length=128)  # Field name made lowercase.
    name = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    urltype = models.IntegerField(db_column='urlType', blank=True, null=True)  # Field name made lowercase.
    weburl = models.CharField(db_column='webUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodscategorygallery'
        unique_together = (('categoryid', 'imageguid'),)


class Goodscateogoryrecommend(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    imgurl = models.CharField(db_column='ImgUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    urltype = models.SmallIntegerField(db_column='UrlType', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isshowtotal = models.IntegerField(db_column='IsShowTotal', blank=True, null=True)  # Field name made lowercase.
    sortindex = models.IntegerField(db_column='SortIndex')  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    lastoperatetime = models.DateTimeField(db_column='LastOperateTime')  # Field name made lowercase.
    lastoperator = models.CharField(db_column='LastOperator', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodscateogoryrecommend'


class Goodscomments(models.Model):
    goodscommentid = models.BigAutoField(db_column='goodsCommentId', primary_key=True)  # Field name made lowercase.
    goodscomment = models.CharField(db_column='goodsComment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ispublicshow = models.IntegerField(db_column='isPublicShow', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    goodscommentpics = models.TextField(db_column='goodsCommentPics', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    srvuserid = models.IntegerField(db_column='srvUserId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    srvcomment = models.CharField(db_column='srvComment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    srvname = models.CharField(db_column='srvName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    srvtime = models.IntegerField(db_column='srvTime', blank=True, null=True)  # Field name made lowercase.
    ordercreatetime = models.PositiveIntegerField(db_column='orderCreateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodscomments'


class Goodsearchkey(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    searchkey = models.CharField(db_column='searchKey', max_length=200, blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeId', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsearchkey'


class Goodsformulacombination(models.Model):
    fcid = models.AutoField(db_column='FCID', primary_key=True)  # Field name made lowercase.
    formulasn = models.CharField(db_column='FormulaSN', max_length=60, blank=True, null=True)  # Field name made lowercase.
    formulaname = models.CharField(db_column='FormulaName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    combsn = models.CharField(db_column='CombSN', max_length=60, blank=True, null=True)  # Field name made lowercase.
    combname = models.CharField(db_column='CombName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    edittime = models.DateTimeField(db_column='EditTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsformulacombination'


class Goodsgallery(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    imageguid = models.CharField(db_column='imageGuid', max_length=64)  # Field name made lowercase.
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    displayindex = models.IntegerField(db_column='displayIndex')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsgallery'


class Goodsinfo(models.Model):
    guid = models.CharField(primary_key=True, max_length=64)
    sn = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=64, blank=True, null=True)
    source = models.CharField(max_length=64, blank=True, null=True)
    barcode = models.CharField(max_length=32, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField()
    stock = models.DecimalField(max_digits=12, decimal_places=2)
    helpcode = models.CharField(db_column='helpCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    brandid = models.IntegerField(db_column='brandId', blank=True, null=True)  # Field name made lowercase.
    venderid = models.IntegerField(db_column='venderId', blank=True, null=True)  # Field name made lowercase.
    vendergoodssn = models.CharField(db_column='venderGoodsSN', max_length=64, blank=True, null=True)  # Field name made lowercase.
    catalogid = models.IntegerField(db_column='catalogId', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    productiondate = models.IntegerField(db_column='productionDate', blank=True, null=True)  # Field name made lowercase.
    shelflife = models.CharField(db_column='shelfLife', max_length=10, blank=True, null=True)  # Field name made lowercase.
    freshdays = models.DecimalField(db_column='freshDays', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mintemperature = models.DecimalField(db_column='minTemperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    maxtemperature = models.DecimalField(db_column='maxTemperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(max_length=16, blank=True, null=True)
    specification = models.CharField(max_length=64, blank=True, null=True)
    byweight = models.TextField(db_column='byWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grade = models.CharField(max_length=16, blank=True, null=True)
    origin1 = models.CharField(max_length=64, blank=True, null=True)
    origin2 = models.CharField(max_length=64, blank=True, null=True)
    level = models.CharField(max_length=32, blank=True, null=True)
    packaged = models.TextField(blank=True, null=True)  # This field type is a guess.
    onsale = models.TextField(db_column='onSale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stockout = models.TextField(db_column='stockOut', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offshelve = models.TextField(db_column='offShelve', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    presale = models.PositiveIntegerField(db_column='preSale', blank=True, null=True)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    descriptiondetail = models.TextField(db_column='descriptionDetail', blank=True, null=True)  # Field name made lowercase.
    packagingdetail = models.TextField(db_column='packagingDetail', blank=True, null=True)  # Field name made lowercase.
    aftersalesdetail = models.TextField(db_column='afterSalesDetail', blank=True, null=True)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    storagecondition = models.CharField(db_column='storageCondition', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rankcount = models.IntegerField(db_column='rankCount', blank=True, null=True)  # Field name made lowercase.
    rank = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)
    warehouse = models.IntegerField(blank=True, null=True)
    issplit = models.TextField(db_column='isSplit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deliverstartdate = models.IntegerField(db_column='deliverStartDate', blank=True, null=True)  # Field name made lowercase.
    deliverenddate = models.IntegerField(db_column='deliverEndDate', blank=True, null=True)  # Field name made lowercase.
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    virtual = models.TextField(blank=True, null=True)  # This field type is a guess.
    goods_id_old = models.IntegerField(blank=True, null=True)
    pinyinfirstletter = models.CharField(db_column='pinYinFirstLetter', max_length=30, blank=True, null=True)  # Field name made lowercase.
    outputtax = models.DecimalField(db_column='outputTax', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    purfrequency = models.IntegerField(db_column='purfreQuency', blank=True, null=True)  # Field name made lowercase.
    distributetimelist = models.CharField(db_column='distributeTimeList', max_length=20, blank=True, null=True)  # Field name made lowercase.
    presalestartdate = models.IntegerField(db_column='preSaleStartDate', blank=True, null=True)  # Field name made lowercase.
    presaleenddate = models.IntegerField(db_column='preSaleEndDate', blank=True, null=True)  # Field name made lowercase.
    wareid = models.BigIntegerField(db_column='wareId', blank=True, null=True)  # Field name made lowercase.
    skuid = models.CharField(db_column='skuId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    food_id = models.IntegerField(blank=True, null=True)
    w_seotitle = models.CharField(db_column='w_seoTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    w_purchaseurl = models.CharField(db_column='w_purchaseUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seopage = models.CharField(db_column='seoPage', max_length=6, blank=True, null=True)  # Field name made lowercase.
    issupackage = models.IntegerField(db_column='isSupackage', blank=True, null=True)  # Field name made lowercase.
    issafebuy = models.IntegerField(db_column='isSafeBuy')  # Field name made lowercase.
    safebuycontent = models.TextField(db_column='safeBuyContent', blank=True, null=True)  # Field name made lowercase.
    safebuyendtime = models.IntegerField(db_column='safeBuyEndTime', blank=True, null=True)  # Field name made lowercase.
    istip = models.IntegerField(db_column='isTip')  # Field name made lowercase.
    tiptitle = models.CharField(db_column='tipTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipcontent = models.TextField(db_column='tipContent', blank=True, null=True)  # Field name made lowercase.
    skuname = models.CharField(db_column='skuName', max_length=255)  # Field name made lowercase.
    isthirdpartygoods = models.IntegerField(db_column='isThirdPartyGoods')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsinfo'


class GoodsinfoBak(models.Model):
    sn = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=16, blank=True, null=True)
    specification = models.CharField(max_length=64, blank=True, null=True)
    onsale = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goodsinfo_bak'


class GoodsinfoBk20170525(models.Model):
    guid = models.CharField(max_length=64)
    sn = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=64, blank=True, null=True)
    source = models.CharField(max_length=64, blank=True, null=True)
    barcode = models.CharField(max_length=32, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField()
    stock = models.DecimalField(max_digits=12, decimal_places=2)
    helpcode = models.CharField(db_column='helpCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    brandid = models.IntegerField(db_column='brandId', blank=True, null=True)  # Field name made lowercase.
    venderid = models.IntegerField(db_column='venderId', blank=True, null=True)  # Field name made lowercase.
    vendergoodssn = models.CharField(db_column='venderGoodsSN', max_length=64, blank=True, null=True)  # Field name made lowercase.
    catalogid = models.IntegerField(db_column='catalogId', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    productiondate = models.IntegerField(db_column='productionDate', blank=True, null=True)  # Field name made lowercase.
    shelflife = models.CharField(db_column='shelfLife', max_length=10, blank=True, null=True)  # Field name made lowercase.
    freshdays = models.DecimalField(db_column='freshDays', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mintemperature = models.DecimalField(db_column='minTemperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    maxtemperature = models.DecimalField(db_column='maxTemperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(max_length=16, blank=True, null=True)
    specification = models.CharField(max_length=64, blank=True, null=True)
    byweight = models.TextField(db_column='byWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grade = models.CharField(max_length=16, blank=True, null=True)
    origin1 = models.CharField(max_length=64, blank=True, null=True)
    origin2 = models.CharField(max_length=64, blank=True, null=True)
    level = models.CharField(max_length=32, blank=True, null=True)
    packaged = models.TextField(blank=True, null=True)  # This field type is a guess.
    onsale = models.TextField(db_column='onSale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stockout = models.TextField(db_column='stockOut', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offshelve = models.TextField(db_column='offShelve', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    presale = models.PositiveIntegerField(db_column='preSale', blank=True, null=True)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    descriptiondetail = models.TextField(db_column='descriptionDetail', blank=True, null=True)  # Field name made lowercase.
    packagingdetail = models.TextField(db_column='packagingDetail', blank=True, null=True)  # Field name made lowercase.
    aftersalesdetail = models.TextField(db_column='afterSalesDetail', blank=True, null=True)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    storagecondition = models.CharField(db_column='storageCondition', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rankcount = models.IntegerField(db_column='rankCount', blank=True, null=True)  # Field name made lowercase.
    rank = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)
    warehouse = models.IntegerField(blank=True, null=True)
    issplit = models.TextField(db_column='isSplit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deliverstartdate = models.IntegerField(db_column='deliverStartDate', blank=True, null=True)  # Field name made lowercase.
    deliverenddate = models.IntegerField(db_column='deliverEndDate', blank=True, null=True)  # Field name made lowercase.
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    virtual = models.TextField(blank=True, null=True)  # This field type is a guess.
    goods_id_old = models.IntegerField(blank=True, null=True)
    pinyinfirstletter = models.CharField(db_column='pinYinFirstLetter', max_length=30, blank=True, null=True)  # Field name made lowercase.
    outputtax = models.DecimalField(db_column='outputTax', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    purfrequency = models.IntegerField(db_column='purfreQuency', blank=True, null=True)  # Field name made lowercase.
    distributetimelist = models.CharField(db_column='distributeTimeList', max_length=20, blank=True, null=True)  # Field name made lowercase.
    presalestartdate = models.IntegerField(db_column='preSaleStartDate', blank=True, null=True)  # Field name made lowercase.
    presaleenddate = models.IntegerField(db_column='preSaleEndDate', blank=True, null=True)  # Field name made lowercase.
    wareid = models.BigIntegerField(db_column='wareId', blank=True, null=True)  # Field name made lowercase.
    skuid = models.CharField(db_column='skuId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    food_id = models.IntegerField(blank=True, null=True)
    w_seotitle = models.CharField(db_column='w_seoTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    w_purchaseurl = models.CharField(db_column='w_purchaseUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seopage = models.CharField(db_column='seoPage', max_length=6, blank=True, null=True)  # Field name made lowercase.
    issupackage = models.IntegerField(db_column='isSupackage', blank=True, null=True)  # Field name made lowercase.
    issafebuy = models.IntegerField(db_column='isSafeBuy')  # Field name made lowercase.
    safebuycontent = models.TextField(db_column='safeBuyContent', blank=True, null=True)  # Field name made lowercase.
    safebuyendtime = models.IntegerField(db_column='safeBuyEndTime', blank=True, null=True)  # Field name made lowercase.
    istip = models.IntegerField(db_column='isTip')  # Field name made lowercase.
    tiptitle = models.CharField(db_column='tipTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipcontent = models.TextField(db_column='tipContent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsinfo_bk20170525'


class GoodsinfoBk20170526(models.Model):
    guid = models.CharField(max_length=64)
    sn = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=64, blank=True, null=True)
    source = models.CharField(max_length=64, blank=True, null=True)
    barcode = models.CharField(max_length=32, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField()
    stock = models.DecimalField(max_digits=12, decimal_places=2)
    helpcode = models.CharField(db_column='helpCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    brandid = models.IntegerField(db_column='brandId', blank=True, null=True)  # Field name made lowercase.
    venderid = models.IntegerField(db_column='venderId', blank=True, null=True)  # Field name made lowercase.
    vendergoodssn = models.CharField(db_column='venderGoodsSN', max_length=64, blank=True, null=True)  # Field name made lowercase.
    catalogid = models.IntegerField(db_column='catalogId', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    productiondate = models.IntegerField(db_column='productionDate', blank=True, null=True)  # Field name made lowercase.
    shelflife = models.CharField(db_column='shelfLife', max_length=10, blank=True, null=True)  # Field name made lowercase.
    freshdays = models.DecimalField(db_column='freshDays', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mintemperature = models.DecimalField(db_column='minTemperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    maxtemperature = models.DecimalField(db_column='maxTemperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(max_length=16, blank=True, null=True)
    specification = models.CharField(max_length=64, blank=True, null=True)
    byweight = models.TextField(db_column='byWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grade = models.CharField(max_length=16, blank=True, null=True)
    origin1 = models.CharField(max_length=64, blank=True, null=True)
    origin2 = models.CharField(max_length=64, blank=True, null=True)
    level = models.CharField(max_length=32, blank=True, null=True)
    packaged = models.TextField(blank=True, null=True)  # This field type is a guess.
    onsale = models.TextField(db_column='onSale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stockout = models.TextField(db_column='stockOut', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offshelve = models.TextField(db_column='offShelve', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    presale = models.PositiveIntegerField(db_column='preSale', blank=True, null=True)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    descriptiondetail = models.TextField(db_column='descriptionDetail', blank=True, null=True)  # Field name made lowercase.
    packagingdetail = models.TextField(db_column='packagingDetail', blank=True, null=True)  # Field name made lowercase.
    aftersalesdetail = models.TextField(db_column='afterSalesDetail', blank=True, null=True)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    storagecondition = models.CharField(db_column='storageCondition', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rankcount = models.IntegerField(db_column='rankCount', blank=True, null=True)  # Field name made lowercase.
    rank = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)
    warehouse = models.IntegerField(blank=True, null=True)
    issplit = models.TextField(db_column='isSplit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deliverstartdate = models.IntegerField(db_column='deliverStartDate', blank=True, null=True)  # Field name made lowercase.
    deliverenddate = models.IntegerField(db_column='deliverEndDate', blank=True, null=True)  # Field name made lowercase.
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    virtual = models.TextField(blank=True, null=True)  # This field type is a guess.
    goods_id_old = models.IntegerField(blank=True, null=True)
    pinyinfirstletter = models.CharField(db_column='pinYinFirstLetter', max_length=30, blank=True, null=True)  # Field name made lowercase.
    outputtax = models.DecimalField(db_column='outputTax', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    purfrequency = models.IntegerField(db_column='purfreQuency', blank=True, null=True)  # Field name made lowercase.
    distributetimelist = models.CharField(db_column='distributeTimeList', max_length=20, blank=True, null=True)  # Field name made lowercase.
    presalestartdate = models.IntegerField(db_column='preSaleStartDate', blank=True, null=True)  # Field name made lowercase.
    presaleenddate = models.IntegerField(db_column='preSaleEndDate', blank=True, null=True)  # Field name made lowercase.
    wareid = models.BigIntegerField(db_column='wareId', blank=True, null=True)  # Field name made lowercase.
    skuid = models.CharField(db_column='skuId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    food_id = models.IntegerField(blank=True, null=True)
    w_seotitle = models.CharField(db_column='w_seoTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    w_purchaseurl = models.CharField(db_column='w_purchaseUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seopage = models.CharField(db_column='seoPage', max_length=6, blank=True, null=True)  # Field name made lowercase.
    issupackage = models.IntegerField(db_column='isSupackage', blank=True, null=True)  # Field name made lowercase.
    issafebuy = models.IntegerField(db_column='isSafeBuy')  # Field name made lowercase.
    safebuycontent = models.TextField(db_column='safeBuyContent', blank=True, null=True)  # Field name made lowercase.
    safebuyendtime = models.IntegerField(db_column='safeBuyEndTime', blank=True, null=True)  # Field name made lowercase.
    istip = models.IntegerField(db_column='isTip')  # Field name made lowercase.
    tiptitle = models.CharField(db_column='tipTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipcontent = models.TextField(db_column='tipContent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsinfo_bk20170526'


class GoodsinfoGoodscategroy(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryId')  # Field name made lowercase.
    level = models.IntegerField()
    goodsalias = models.CharField(db_column='goodsAlias', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsinfo_goodscategroy'


class GoodsinfoGoodscategroy20170425(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryId')  # Field name made lowercase.
    level = models.IntegerField()
    goodsalias = models.CharField(db_column='goodsAlias', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsinfo_goodscategroy_20170425'


class Goodsoffshelvechangelog(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    originaloffshelve = models.TextField(db_column='originalOffShelve')  # Field name made lowercase. This field type is a guess.
    offshelve = models.TextField(db_column='offShelve')  # Field name made lowercase. This field type is a guess.
    updatedtime = models.IntegerField(db_column='updatedTime')  # Field name made lowercase.
    operator = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsoffshelvechangelog'


class Goodsonsalechangelog(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    originalonsale = models.TextField(db_column='originalOnSale')  # Field name made lowercase. This field type is a guess.
    onsale = models.TextField(db_column='onSale')  # Field name made lowercase. This field type is a guess.
    updatedtime = models.IntegerField(db_column='updatedTime')  # Field name made lowercase.
    operator = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsonsalechangelog'


class Goodspackageitem(models.Model):
    packageguid = models.CharField(db_column='packageGuid', max_length=64)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    displayindex = models.IntegerField(db_column='displayIndex')  # Field name made lowercase.
    count = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'goodspackageitem'


class Goodsplan(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goodsplan'


class Goodsplangallery(models.Model):
    targetid = models.CharField(db_column='targetId', max_length=128)  # Field name made lowercase.
    imageguid = models.CharField(db_column='imageGuid', max_length=64)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsplangallery'


class Goodsprice(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(max_length=32, blank=True, null=True)
    profitrate = models.DecimalField(db_column='profitRate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    general = models.TextField(blank=True, null=True)  # This field type is a guess.
    propertyidsequence = models.CharField(db_column='propertyIdSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    propertynamesequence = models.CharField(db_column='propertyNameSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    optionidsequence = models.CharField(db_column='optionIdSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    optionnamesequence = models.CharField(db_column='optionNameSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsprice'


class Goodspriceadjustment(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    requiredby = models.IntegerField(db_column='requiredBy')  # Field name made lowercase.
    requireddate = models.IntegerField(db_column='requiredDate')  # Field name made lowercase.
    approved = models.TextField(blank=True, null=True)  # This field type is a guess.
    approvedby = models.IntegerField(db_column='approvedBy', blank=True, null=True)  # Field name made lowercase.
    approveddate = models.IntegerField(db_column='approvedDate', blank=True, null=True)  # Field name made lowercase.
    approvednote = models.CharField(db_column='approvedNote', max_length=500, blank=True, null=True)  # Field name made lowercase.
    iseffect = models.TextField(db_column='isEffect', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isrestore = models.TextField(db_column='isRestore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    isrestoreprice = models.IntegerField(db_column='isRestorePrice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodspriceadjustment'


class Goodspriceadjustmentdetail(models.Model):
    adjustmentid = models.IntegerField(db_column='adjustmentId', blank=True, null=True)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    priceproperty = models.CharField(db_column='priceProperty', max_length=64, blank=True, null=True)  # Field name made lowercase.
    originalprice = models.DecimalField(db_column='originalPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    requiredprice = models.DecimalField(db_column='requiredPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalprofitrate = models.DecimalField(db_column='originalProfitRate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    requiredprofitrate = models.DecimalField(db_column='requiredProfitRate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    requiredpricerate = models.DecimalField(db_column='requiredPriceRate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalcost = models.DecimalField(db_column='originalCost', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    requiredcost = models.DecimalField(db_column='requiredCost', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    requiredcostrate = models.DecimalField(db_column='requiredCostRate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    requirednote = models.CharField(db_column='requiredNote', max_length=500, blank=True, null=True)  # Field name made lowercase.
    general = models.TextField(blank=True, null=True)  # This field type is a guess.
    originalmarketprice = models.DecimalField(db_column='originalMarketPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    requiredmarketprice = models.DecimalField(db_column='requiredMarketPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    requiredmarketpricerate = models.DecimalField(db_column='requiredMarketPriceRate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodspriceadjustmentdetail'


class Goodspriceapproval(models.Model):
    supervisorid = models.CharField(db_column='supervisorId', max_length=64)  # Field name made lowercase.
    maxrate = models.DecimalField(db_column='maxRate', max_digits=10, decimal_places=2)  # Field name made lowercase.
    deleted = models.TextField()  # This field type is a guess.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodspriceapproval'


class Goodspromotion(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(max_length=32, blank=True, null=True)
    promotionid = models.IntegerField(db_column='promotionId', blank=True, null=True)  # Field name made lowercase.
    promotiontype = models.CharField(db_column='promotionType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    promotiontitle = models.CharField(db_column='promotionTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotionprice = models.DecimalField(db_column='promotionPrice', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodspromotion'


class Goodsproperty(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsproperty'


class Goodspropertyoption(models.Model):
    propertyid = models.IntegerField(db_column='propertyId')  # Field name made lowercase.
    name = models.CharField(max_length=64)
    enabled = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goodspropertyoption'


class Goodspropertysetting(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    propertyidsequence = models.CharField(db_column='propertyIdSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    propertynamesequence = models.CharField(db_column='propertyNameSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    optionidsequence = models.CharField(db_column='optionIdSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    optionnamesequence = models.CharField(db_column='optionNameSequence', max_length=256, blank=True, null=True)  # Field name made lowercase.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    sku = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodspropertysetting'


class Goodssaleqty(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    totalqty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodssaleqty'


class Goodssaleschedule(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    name = models.CharField(max_length=64)
    startdate = models.IntegerField(db_column='startDate')  # Field name made lowercase.
    enddate = models.IntegerField(db_column='endDate')  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodssaleschedule'


class Goodssaletag(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    groupid = models.IntegerField(db_column='groupId', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodssaletag'


class Goodssaletaggroup(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isrelatedtocount = models.TextField(db_column='isRelatedToCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodssaletaggroup'


class Goodssatisfy(models.Model):
    pid = models.BigAutoField(db_column='id',primary_key=True)
    orderid = models.IntegerField(db_column='orderId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    goodssatisfylevel = models.SmallIntegerField(db_column='goodsSatisfyLevel', blank=True, null=True)  # Field name made lowercase.
    ispublicshow = models.IntegerField(db_column='isPublicShow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodssatisfy'


class Goodsseoinfo(models.Model):
    sn = models.CharField(primary_key=True, max_length=64)
    title = models.CharField(max_length=100, blank=True, null=True)
    key_word = models.CharField(max_length=200, blank=True, null=True)
    descp = models.CharField(max_length=3000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsseoinfo'


class Goodsshelf(models.Model):
    name = models.CharField(max_length=64)
    templateid = models.IntegerField(db_column='templateId')  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=64, blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.
    settings = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsshelf'


class Goodsshelfitem(models.Model):
    pid = models.IntegerField(db_column='id',primary_key=True)
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    shelfid = models.IntegerField(db_column='shelfId', blank=True, null=True)  # Field name made lowercase.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsshelfitem'


class Goodsshelftemplate(models.Model):
    name = models.CharField(max_length=64)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    targetplatform = models.IntegerField(db_column='targetPlatform', blank=True, null=True)  # Field name made lowercase.
    createddate = models.IntegerField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsshelftemplate'


class Goodsstock(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    storagestock = models.DecimalField(db_column='storageStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    safystock = models.DecimalField(db_column='safyStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salablestock = models.DecimalField(db_column='salableStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soldstock = models.DecimalField(db_column='soldStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    availablestock = models.DecimalField(db_column='availableStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    frozenstock = models.DecimalField(db_column='frozenStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime')  # Field name made lowercase.
    general = models.TextField(blank=True, null=True)  # This field type is a guess.
    propertyidsequence = models.CharField(db_column='propertyIdSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    propertynamesequence = models.CharField(db_column='propertyNameSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    optionidsequence = models.CharField(db_column='optionIdSequence', max_length=128, blank=True, null=True)  # Field name made lowercase.
    optionnamesequence = models.CharField(db_column='optionNameSequence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stocktype = models.IntegerField(db_column='stockType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsstock'


class Goodsstockchangelog(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    general = models.TextField(blank=True, null=True)  # This field type is a guess.
    stocktype = models.IntegerField(db_column='stockType', blank=True, null=True)  # Field name made lowercase.
    storagestock = models.DecimalField(db_column='storageStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    safystock = models.DecimalField(db_column='safyStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salablestock = models.DecimalField(db_column='salableStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soldstock = models.DecimalField(db_column='soldStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    availablestock = models.DecimalField(db_column='availableStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    frozenstock = models.DecimalField(db_column='frozenStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalstoragestock = models.DecimalField(db_column='originalStorageStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalsafystock = models.DecimalField(db_column='originalSafyStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalsalablestock = models.DecimalField(db_column='originalSalableStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalsoldstock = models.DecimalField(db_column='originalSoldStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalavailablestock = models.DecimalField(db_column='originalAvailableStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    originalfrozenstock = models.DecimalField(db_column='originalFrozenStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsstockchangelog'


class Goodsstocktemporary(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    salablestock = models.DecimalField(db_column='salableStock', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stocktype = models.IntegerField(db_column='stockType', blank=True, null=True)  # Field name made lowercase.
    general = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.CharField(max_length=64, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsstocktemporary'


class Goodssupackage(models.Model):
    sugoodsguid = models.CharField(db_column='suGoodsGuid', max_length=50)  # Field name made lowercase.
    susn = models.CharField(db_column='suSn', max_length=255)  # Field name made lowercase.
    suname = models.CharField(db_column='suName', max_length=50)  # Field name made lowercase.
    combgoodsguid = models.CharField(db_column='combGoodsGuid', max_length=50)  # Field name made lowercase.
    combsn = models.CharField(db_column='combSn', max_length=255)  # Field name made lowercase.
    combname = models.CharField(db_column='combName', max_length=255)  # Field name made lowercase.
    unit = models.CharField(max_length=50, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodssupackage'


class Goodssyncstatus(models.Model):
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    scheduledtime = models.IntegerField(db_column='scheduledTime')  # Field name made lowercase.
    synchronizedtime = models.IntegerField(db_column='synchronizedTime', blank=True, null=True)  # Field name made lowercase.
    verifiedtime = models.IntegerField(db_column='verifiedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodssyncstatus'


class Goodsvender(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    zipcode = models.CharField(db_column='zipCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    vendorid = models.CharField(db_column='vendorId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodsvender'


class Goodwatermarkicon(models.Model):
    watermarkid = models.AutoField(db_column='watermarkId', primary_key=True)  # Field name made lowercase.
    watermarkname = models.CharField(db_column='watermarkName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    imageguid = models.CharField(db_column='imageGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    watermarkdesc = models.CharField(db_column='watermarkDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodwatermarkicon'


class H5Vouchercode(models.Model):
    voucherid = models.AutoField(db_column='voucherId', primary_key=True)  # Field name made lowercase.
    vouchercode = models.CharField(db_column='voucherCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    isused = models.IntegerField(db_column='isUsed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h5vouchercode'


class Image(models.Model):
    guid = models.CharField(primary_key=True, max_length=64)
    url = models.CharField(max_length=512)
    width = models.IntegerField()
    height = models.IntegerField()
    size = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=8)
    description = models.TextField(blank=True, null=True)
    referencetype = models.CharField(db_column='referenceType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referencecount = models.IntegerField(db_column='referenceCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'image'


class Imgverificationcode(models.Model):
    imgid = models.AutoField(db_column='imgId', primary_key=True)  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imgverificationcode'


class Importcompanymemberhistory(models.Model):
    pid = models.BigAutoField(db_column='id',primary_key=True)
    account = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    channel = models.CharField(max_length=100, blank=True, null=True)
    campaign = models.CharField(max_length=500, blank=True, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createuser = models.CharField(db_column='createUser', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'importcompanymemberhistory'


class Importmemberhistory(models.Model):
    pid = models.CharField(db_column='id',primary_key=True, max_length=64)
    account = models.CharField(max_length=255)
    level = models.IntegerField(blank=True, null=True)
    invitationcode = models.CharField(db_column='invitationCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(max_length=512, blank=True, null=True)
    createuser = models.CharField(db_column='createUser', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'importmemberhistory'


class Invitationcodeshowinfo(models.Model):
    pagetitle = models.CharField(db_column='pageTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invitationcodetypeid = models.IntegerField(db_column='invitationcodetypeId', blank=True, null=True)  # Field name made lowercase.
    headimageurl = models.CharField(db_column='headimageUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    activitydesc = models.CharField(db_column='activityDesc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    footimageurl = models.CharField(db_column='footimageUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    strattime = models.DateTimeField(db_column='stratTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(blank=True, null=True)
    headimageurl2 = models.CharField(db_column='headimageUrl2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    activitydesc2 = models.CharField(db_column='activityDesc2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    activitydesc3 = models.CharField(db_column='activityDesc3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    expiredimageurl = models.CharField(db_column='expiredimageUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invitationcodeshowinfo'


class Invoicetitle(models.Model):
    invoiceid = models.AutoField(db_column='invoiceId', primary_key=True)  # Field name made lowercase.
    invoicetype = models.IntegerField(db_column='invoiceType', blank=True, null=True)  # Field name made lowercase.
    titlename = models.CharField(db_column='titleName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxidentificationnum = models.CharField(db_column='taxIdentificationNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoicetitle'


class JdInvokingapilog(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    requestmessage = models.CharField(db_column='requestMessage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    returnmessage = models.CharField(db_column='returnMessage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jd_invokingapilog'


class Jdcoupondetail(models.Model):
    orderid = models.PositiveIntegerField(db_column='orderId')  # Field name made lowercase.
    outorderid = models.CharField(db_column='outOrderId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    skuid = models.CharField(db_column='skuId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    coupontype = models.CharField(db_column='couponType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    couponprice = models.DecimalField(db_column='couponPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jdcoupondetail'


class Mailtemplate(models.Model):
    templatecode = models.CharField(db_column='templateCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(max_length=256, blank=True, null=True)
    mailto = models.CharField(db_column='mailTo', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailcc = models.CharField(db_column='mailCc', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailbcc = models.CharField(db_column='mailBcc', max_length=256, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    enable = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    createat = models.DateTimeField(blank=True, null=True)
    createby = models.IntegerField(blank=True, null=True)
    updateat = models.DateTimeField(blank=True, null=True)
    updateby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailtemplate'


class MambercashcardUpdate(models.Model):
    carno = models.CharField(db_column='carNo', max_length=64, blank=True, null=True)  # Field name made lowercase.
    usetime = models.IntegerField(db_column='useTime', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mambercashcard_update'


class McGroupcode(models.Model):
    groupcode = models.CharField(max_length=50)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_groupcode'
        unique_together = (('id', 'groupcode'),)


class McGroupleader(models.Model):
    mobile = models.CharField(max_length=20, blank=True, null=True)
    groupnumber = models.IntegerField(blank=True, null=True)
    finishsendmsg = models.IntegerField(blank=True, null=True)
    sendmsgtime = models.DateTimeField(blank=True, null=True)
    groupcodename = models.CharField(max_length=50, blank=True, null=True)
    groupcodeid = models.IntegerField(db_column='groupcodeId', blank=True, null=True)  # Field name made lowercase.
    grouplistid = models.IntegerField(blank=True, null=True)
    longitude = models.CharField(db_column='Longitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(blank=True, null=True)
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    invitedcode = models.CharField(db_column='invitedCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grouphour = models.IntegerField(db_column='GroupHour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mc_groupleader'


class McGrouplist(models.Model):
    groupname = models.CharField(max_length=50, blank=True, null=True)
    groupnumber = models.IntegerField(blank=True, null=True)
    begintime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    enable = models.TextField(blank=True, null=True)  # This field type is a guess.
    limitcount = models.IntegerField(blank=True, null=True)
    goodssn = models.CharField(db_column='goodsSn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(blank=True, null=True)
    shippingtimerule = models.CharField(db_column='shippingTimeRule', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    groupfinish = models.IntegerField(db_column='GroupFinish', blank=True, null=True)  # Field name made lowercase.
    grouprule = models.CharField(db_column='GroupRule', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sharedata = models.CharField(db_column='ShareData', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    grouptype = models.IntegerField(db_column='GroupType', blank=True, null=True)  # Field name made lowercase.
    grouphour = models.IntegerField(db_column='GroupHour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mc_grouplist'


class McGroupmember(models.Model):
    mobile = models.CharField(max_length=20, blank=True, null=True)
    groupcodename = models.CharField(max_length=15, blank=True, null=True)
    groupleaderid = models.IntegerField(db_column='groupleaderId', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(blank=True, null=True)
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    grouplistid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_groupmember'


class Mediareport(models.Model):
    reportid = models.AutoField(db_column='reportId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=200, blank=True, null=True)
    redirecturl = models.CharField(db_column='redirectUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    medianame = models.CharField(db_column='mediaName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reporttime = models.IntegerField(db_column='reportTime', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.IntegerField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mediareport'


class Meituanorderrelate(models.Model):
    orderid = models.CharField(db_column='orderId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderidview = models.CharField(db_column='orderIdView', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'meituanorderrelate'


class Member(models.Model):
    pid = models.CharField(db_column='id',primary_key=True, max_length=64)
    account = models.CharField(unique=True, max_length=64, blank=True, null=True)
    password = models.CharField(max_length=127, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    registrationchannel = models.IntegerField(db_column='registrationChannel', blank=True, null=True)  # Field name made lowercase.
    signupdate = models.IntegerField(db_column='signupDate', blank=True, null=True)  # Field name made lowercase.
    salt = models.CharField(max_length=32)
    user_id_old = models.IntegerField(blank=True, null=True)
    refreshdate = models.DateTimeField(db_column='refreshDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class MemberImport(models.Model):
    account = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    salt = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_import'


class MemberMembergroup(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_membergroup'


class MemberMessage(models.Model):
    messageid = models.IntegerField(db_column='messageId', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_message'


class MemberPasswordUpdate(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_password_update'


class Memberaccount(models.Model):
    memberid = models.CharField(db_column='memberId', primary_key=True, max_length=64)  # Field name made lowercase.
    score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    emoney = models.DecimalField(db_column='eMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vouchercount = models.IntegerField(db_column='voucherCount', blank=True, null=True)  # Field name made lowercase.
    experience = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    wochuscore = models.IntegerField(db_column='wochuScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberaccount'


class MemberaccountPointsUpdate(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    pay_points = models.IntegerField(blank=True, null=True)
    user_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memberaccount_points_update'


class Memberaddress(models.Model):
    addressname = models.CharField(db_column='addressName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    consignee = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    tel = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=127, blank=True, null=True)
    oldregion = models.CharField(db_column='oldRegion', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    eventtype = models.PositiveIntegerField(db_column='eventType', blank=True, null=True)  # Field name made lowercase.
    sitesn = models.CharField(db_column='siteSN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    default = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    user_id_old = models.IntegerField(blank=True, null=True)
    address_id_old = models.IntegerField(blank=True, null=True)
    streetnumber = models.CharField(db_column='streetNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    positionresult = models.IntegerField(db_column='positionResult', blank=True, null=True)  # Field name made lowercase.
    isdefaults = models.IntegerField(db_column='isDefaults', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='isValid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberaddress'


class Memberamountchangelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    isgroup = models.TextField(db_column='isGroup', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operator = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    referenceid = models.IntegerField(db_column='referenceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberamountchangelog'


class Memberbalancechangelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    originalbalance = models.DecimalField(db_column='originalBalance', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    newbalance = models.DecimalField(db_column='newBalance', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    reason = models.CharField(max_length=127, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberbalancechangelog'


class Memberbinding(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=128)  # Field name made lowercase.
    openid = models.CharField(db_column='openId', max_length=128)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberbinding'


class Memberblacklist(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(max_length=32, blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    reason = models.CharField(max_length=127, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberblacklist'


class Membercashcard(models.Model):
    cardno = models.CharField(db_column='cardNo', max_length=64, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=128, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    importby = models.CharField(db_column='importBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    importedtime = models.IntegerField(db_column='importedTime', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    usedtime = models.IntegerField(db_column='usedTime', blank=True, null=True)  # Field name made lowercase.
    currency = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    batchno = models.CharField(db_column='batchNo', max_length=128, blank=True, null=True)  # Field name made lowercase.
    expiredtime = models.IntegerField(db_column='expiredTime', blank=True, null=True)  # Field name made lowercase.
    card_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membercashcard'


class Membercomment(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    targetid = models.CharField(db_column='targetId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membercomment'


class Memberemoneychangelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    emoney = models.DecimalField(db_column='eMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberemoneychangelog'


class Memberfavorite(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    targetid = models.CharField(db_column='targetId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberfavorite'


class Memberfork(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    targetid = models.CharField(db_column='targetId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    targettype = models.IntegerField(db_column='targetType', blank=True, null=True)  # Field name made lowercase.
    like = models.TextField(blank=True, null=True)  # This field type is a guess.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberfork'


class Memberfromreach(models.Model):
    cardnumber = models.CharField(db_column='cardNumber', max_length=255)  # Field name made lowercase.
    telephone = models.CharField(max_length=50)
    usertype = models.IntegerField(db_column='userType')  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    isidentifymember = models.TextField(db_column='isIdentifyMember', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identifymembertime = models.DateTimeField(db_column='identifyMemberTime', blank=True, null=True)  # Field name made lowercase.
    identifymembersource = models.CharField(db_column='identifyMemberSource', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isidentifylevel = models.PositiveIntegerField(db_column='isIdentifyLevel', blank=True, null=True)  # Field name made lowercase.
    identifyleveltime = models.DateTimeField(db_column='identifyLevelTime', blank=True, null=True)  # Field name made lowercase.
    identifylevelsource = models.CharField(db_column='identifyLevelSource', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberfromreach'


class Membergroup(models.Model):
    name = models.CharField(max_length=36, blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membergroup'


class Memberinfo(models.Model):
    memberid = models.CharField(db_column='memberId', primary_key=True, max_length=64)  # Field name made lowercase.
    alias = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.CharField(max_length=127, blank=True, null=True)
    birthday = models.IntegerField(blank=True, null=True)
    zipcode = models.CharField(db_column='zipCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=15, blank=True, null=True)
    identityno = models.CharField(db_column='identityNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    identitytype = models.IntegerField(db_column='identityType', blank=True, null=True)  # Field name made lowercase.
    cardno = models.CharField(db_column='cardNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    firsttimelogin = models.IntegerField(db_column='firstTimeLogin', blank=True, null=True)  # Field name made lowercase.
    haspassword = models.TextField(db_column='hasPassword', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invitationcode = models.CharField(db_column='invitationCode', max_length=127, blank=True, null=True)  # Field name made lowercase.
    invitedcode = models.CharField(db_column='invitedCode', max_length=127, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    lastloginversion = models.CharField(db_column='lastLoginVersion', max_length=16, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    user_id_old = models.IntegerField(blank=True, null=True)
    isreturnscore = models.TextField(db_column='isReturnScore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel = models.CharField(max_length=100, blank=True, null=True)
    campaign = models.CharField(max_length=500, blank=True, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)
    phonemodel = models.CharField(db_column='phoneModel', max_length=128, blank=True, null=True)  # Field name made lowercase.
    systemversion = models.CharField(db_column='systemVersion', max_length=128, blank=True, null=True)  # Field name made lowercase.
    phoneidentifier = models.CharField(db_column='phoneIdentifier', max_length=128, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(max_length=128, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    adcid = models.CharField(db_column='adcId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    adid = models.PositiveIntegerField(db_column='adId', blank=True, null=True)  # Field name made lowercase.
    errorpaymentpasswordstarttime = models.IntegerField(db_column='errorPaymentPasswordStartTime', blank=True, null=True)  # Field name made lowercase.
    paymentpassworderrornum = models.IntegerField(db_column='paymentPasswordErrorNum', blank=True, null=True)  # Field name made lowercase.
    paymentpassword = models.CharField(db_column='paymentPassword', max_length=127, blank=True, null=True)  # Field name made lowercase.
    isnewcustomer = models.TextField(db_column='isNewCustomer')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'memberinfo'


class MemberinfoCopy(models.Model):
    memberid = models.CharField(db_column='memberId', primary_key=True, max_length=64)  # Field name made lowercase.
    alias = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.CharField(max_length=127, blank=True, null=True)
    birthday = models.IntegerField(blank=True, null=True)
    zipcode = models.CharField(db_column='zipCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=15, blank=True, null=True)
    identityno = models.CharField(db_column='identityNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    identitytype = models.IntegerField(db_column='identityType', blank=True, null=True)  # Field name made lowercase.
    cardno = models.CharField(db_column='cardNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    firsttimelogin = models.IntegerField(db_column='firstTimeLogin', blank=True, null=True)  # Field name made lowercase.
    haspassword = models.TextField(db_column='hasPassword', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invitationcode = models.CharField(db_column='invitationCode', max_length=127, blank=True, null=True)  # Field name made lowercase.
    invitedcode = models.CharField(db_column='invitedCode', max_length=127, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    lastloginversion = models.CharField(db_column='lastLoginVersion', max_length=16, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    user_id_old = models.IntegerField(blank=True, null=True)
    isreturnscore = models.TextField(db_column='isReturnScore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel = models.CharField(max_length=100, blank=True, null=True)
    campaign = models.CharField(max_length=500, blank=True, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)
    phonemodel = models.CharField(db_column='phoneModel', max_length=128, blank=True, null=True)  # Field name made lowercase.
    systemversion = models.CharField(db_column='systemVersion', max_length=128, blank=True, null=True)  # Field name made lowercase.
    phoneidentifier = models.CharField(db_column='phoneIdentifier', max_length=128, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(max_length=128, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    adcid = models.CharField(db_column='adcId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    adid = models.PositiveIntegerField(db_column='adId', blank=True, null=True)  # Field name made lowercase.
    errorpaymentpasswordstarttime = models.IntegerField(db_column='errorPaymentPasswordStartTime', blank=True, null=True)  # Field name made lowercase.
    paymentpassworderrornum = models.IntegerField(db_column='paymentPasswordErrorNum', blank=True, null=True)  # Field name made lowercase.
    paymentpassword = models.CharField(db_column='paymentPassword', max_length=127, blank=True, null=True)  # Field name made lowercase.
    isnewcustomer = models.TextField(db_column='isNewCustomer')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'memberinfo_copy'


class Memberinfoinvitetmp(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    invitationcode = models.CharField(db_column='invitationCode', max_length=127, blank=True, null=True)  # Field name made lowercase.
    invitedcode = models.CharField(db_column='invitedCode', max_length=127, blank=True, null=True)  # Field name made lowercase.
    invitationcode_old = models.CharField(db_column='invitationCode_old', max_length=127, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberinfoinvitetmp'


class Memberinvitationcode(models.Model):
    invitationcode = models.CharField(primary_key=True, max_length=128)
    type = models.IntegerField(blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberinvitationcode'


class Memberinvitationcodetype(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    reward = models.CharField(max_length=400, blank=True, null=True)
    smscontent = models.CharField(db_column='SMScontent', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberinvitationcodetype'


class Memberinvoice(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    invoicetype = models.CharField(db_column='invoiceType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    invoicepayee = models.CharField(db_column='invoicePayee', max_length=120, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberinvoice'


class Memberinvoiceemail(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=128, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberinvoiceemail'


class Memberlevel(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=64, blank=True, null=True)
    minexp = models.IntegerField(db_column='minExp', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberlevel'


class Memberlevelchangelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    originallevelid = models.IntegerField(db_column='originalLevelId', blank=True, null=True)  # Field name made lowercase.
    newlevelid = models.IntegerField(db_column='newLevelId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=32, blank=True, null=True)
    reason = models.CharField(max_length=127, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberlevelchangelog'


class Memberlock(models.Model):
    memberid = models.CharField(db_column='memberId', primary_key=True, max_length=64)  # Field name made lowercase.
    account = models.CharField(max_length=64, blank=True, null=True)
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    reason = models.CharField(max_length=127, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberlock'


class Memberloginerrorlog(models.Model):
    account = models.CharField(max_length=64)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberloginerrorlog'


class Membermessageclose(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=255)  # Field name made lowercase.
    messagetype = models.IntegerField(db_column='messageType', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membermessageclose'


class Membermessagetype(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'membermessagetype'


class Memberreachchangelog(models.Model):
    cardnumber = models.CharField(db_column='cardNumber', max_length=255)  # Field name made lowercase.
    telephoneold = models.CharField(max_length=50)
    telephonenew = models.CharField(max_length=50, blank=True, null=True)
    usertypeold = models.IntegerField(db_column='userTypeold')  # Field name made lowercase.
    usertypenew = models.IntegerField(db_column='userTypenew')  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberreachchangelog'


class Memberreturnscorebak(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    isreturnscore = models.TextField(db_column='isReturnScore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'memberreturnscorebak'


class Memberscorechangelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    isgroup = models.TextField(db_column='isGroup', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operator = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    referenceid = models.IntegerField(db_column='referenceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberscorechangelog'


class Membersecurity(models.Model):
    memberid = models.CharField(db_column='memberId', primary_key=True, max_length=64)  # Field name made lowercase.
    question1 = models.CharField(max_length=127, blank=True, null=True)
    answer1 = models.CharField(max_length=127, blank=True, null=True)
    question2 = models.CharField(max_length=127, blank=True, null=True)
    answer2 = models.CharField(max_length=127, blank=True, null=True)
    question3 = models.CharField(max_length=127, blank=True, null=True)
    answer3 = models.CharField(max_length=127, blank=True, null=True)
    failuretimes = models.IntegerField(db_column='failureTimes', blank=True, null=True)  # Field name made lowercase.
    lastlogintime = models.IntegerField(db_column='lastLoginTime', blank=True, null=True)  # Field name made lowercase.
    lastloginip = models.CharField(db_column='lastLoginIp', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membersecurity'


class Membershippingtime(models.Model):
    memberid = models.CharField(db_column='memberId', primary_key=True, max_length=64)  # Field name made lowercase.
    shippingdate = models.IntegerField(db_column='shippingDate', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.CharField(db_column='shippingTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addressid = models.IntegerField(db_column='addressId')  # Field name made lowercase.
    isdfault = models.IntegerField(db_column='isDfault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membershippingtime'


class Membershippingtimelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shippingdate = models.DateTimeField(db_column='shippingDate', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.CharField(db_column='shippingTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membershippingtimelog'


class Membervoucher(models.Model):
    voucherid = models.CharField(db_column='voucherId', primary_key=True, max_length=128)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    order_id_old = models.IntegerField(blank=True, null=True)
    coupon_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membervoucher'
        unique_together = (('voucherid', 'memberid'),)


class MembervoucherBkFor0102(models.Model):
    voucherid = models.CharField(db_column='voucherId', max_length=128)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    order_id_old = models.IntegerField(blank=True, null=True)
    coupon_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membervoucher_bk_for01_02'


class MembervoucherHistory(models.Model):
    voucherid = models.CharField(db_column='voucherId', primary_key=True, max_length=128)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    order_id_old = models.IntegerField(blank=True, null=True)
    coupon_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membervoucher_history'
        unique_together = (('voucherid', 'memberid'),)


class MembervoucherImport(models.Model):
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    sn = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membervoucher_import'


class MembervoucherUpdate(models.Model):
    voucherid = models.CharField(db_column='voucherId', primary_key=True, max_length=128)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membervoucher_update'
        unique_together = (('voucherid', 'memberid'),)


class Membervoucherusagelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    voucherid = models.CharField(db_column='voucherId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vouchertype = models.IntegerField(db_column='voucherType', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    order_id_old = models.IntegerField(blank=True, null=True)
    coupon_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membervoucherusagelog'


class Memberwochuscorechangelog(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    score = models.IntegerField()
    originalscore = models.IntegerField(db_column='originalScore')  # Field name made lowercase.
    newscore = models.IntegerField(db_column='newScore')  # Field name made lowercase.
    type = models.IntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    operator = models.CharField(max_length=64, blank=True, null=True)
    reason = models.CharField(max_length=2048, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberwochuscorechangelog'


class Message(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    messagetype = models.IntegerField(db_column='messageType')  # Field name made lowercase.
    pictureurl = models.CharField(db_column='pictureUrl', max_length=512, blank=True, null=True)  # Field name made lowercase.
    redirecturl = models.CharField(db_column='redirectUrl', max_length=512, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(max_length=64)
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Messagequeueoperatelog(models.Model):
    project = models.CharField(max_length=255, blank=True, null=True)
    modulename = models.CharField(max_length=255, blank=True, null=True)
    routing = models.CharField(max_length=255, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.CharField(max_length=4000, blank=True, null=True)
    issuccess = models.PositiveIntegerField(blank=True, null=True)
    createdtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messagequeueoperatelog'


class Messagequeueorderlog(models.Model):
    ordersn = models.CharField(db_column='orderSn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messagequeueorderlog'


class Need1(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=66, blank=True, null=True)  # Field name made lowercase.
    account = models.BigIntegerField(blank=True, null=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'need1'


class Need3(models.Model):
    memberid = models.CharField(max_length=66, blank=True, null=True)
    account = models.BigIntegerField(blank=True, null=True)
    templateid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'need3'


class OActivity(models.Model):
    pid = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    activity_title = models.CharField(db_column='ACTIVITY_TITLE', max_length=200)  # Field name made lowercase.
    serial_no = models.CharField(db_column='SERIAL_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    begin_time = models.DateTimeField(db_column='BEGIN_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    banner_pic = models.CharField(db_column='BANNER_PIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    list_pic = models.CharField(db_column='LIST_PIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    share_pic = models.CharField(db_column='SHARE_PIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_seat = models.IntegerField(db_column='TOTAL_SEAT', blank=True, null=True)  # Field name made lowercase.
    participants_num = models.IntegerField(db_column='PARTICIPANTS_NUM', blank=True, null=True)  # Field name made lowercase.
    confirm_num = models.IntegerField(db_column='CONFIRM_NUM', blank=True, null=True)  # Field name made lowercase.
    cate = models.ForeignKey(DActCategory, models.DO_NOTHING, db_column='CATE_ID', blank=True, null=True)  # Field name made lowercase.
    context_path = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey(DActStatus, models.DO_NOTHING, db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insert_timestamp = models.DateTimeField(db_column='INSERT_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    inserted_by = models.IntegerField(db_column='INSERTED_BY', blank=True, null=True)  # Field name made lowercase.
    updated_timestamp = models.DateTimeField(db_column='UPDATED_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.IntegerField(db_column='UPDATED_BY', blank=True, null=True)  # Field name made lowercase.
    pav = models.ForeignKey('OPavilion', models.DO_NOTHING, db_column='PAV_ID', blank=True, null=True)  # Field name made lowercase.
    seq = models.DecimalField(db_column='SEQ', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    need_reg = models.CharField(db_column='NEED_REG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'o_activity'


class ODish(models.Model):
    dish_code = models.CharField(db_column='DISH_CODE', primary_key=True, max_length=50)  # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    menu_name = models.CharField(db_column='MENU_NAME', max_length=100)  # Field name made lowercase.
    slogan = models.CharField(db_column='SLOGAN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descp = models.TextField(db_column='DESCP', blank=True, null=True)  # Field name made lowercase.
    cook_time = models.IntegerField(db_column='COOK_TIME', blank=True, null=True)  # Field name made lowercase.
    diff_index = models.IntegerField(db_column='DIFF_INDEX', blank=True, null=True)  # Field name made lowercase.
    meals_num_down = models.IntegerField(db_column='MEALS_NUM_DOWN', blank=True, null=True)  # Field name made lowercase.
    meals_num_up = models.IntegerField(db_column='MEALS_NUM_UP', blank=True, null=True)  # Field name made lowercase.
    begin_time = models.CharField(db_column='BEGIN_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    end_time = models.CharField(db_column='END_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    insert_by = models.IntegerField(db_column='INSERT_BY', blank=True, null=True)  # Field name made lowercase.
    insert_timestamp = models.DateTimeField(db_column='INSERT_TIMESTAMP')  # Field name made lowercase.
    update_by = models.IntegerField(db_column='UPDATE_BY', blank=True, null=True)  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='UPDATE_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    taste = models.CharField(max_length=40, blank=True, null=True)
    cook_arts = models.CharField(max_length=40, blank=True, null=True)
    search_count = models.IntegerField(db_column='SEARCH_COUNT', blank=True, null=True)  # Field name made lowercase.
    deleted = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'o_dish'


class OEggActivity(models.Model):
    activity_name = models.CharField(max_length=50, blank=True, null=True)
    voucher_prefix = models.CharField(max_length=30)
    voucher_start_pos = models.CharField(max_length=30)
    voucher_total = models.IntegerField()
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    insert_by = models.CharField(max_length=128, blank=True, null=True)
    insert_timestamp = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=128, blank=True, null=True)
    update_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_egg_activity'


class OHotsale(models.Model):
    hotsale_id = models.CharField(db_column='HotSale_ID', primary_key=True, max_length=64)  # Field name made lowercase.
    product_productid = models.CharField(db_column='product_productId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    product_title = models.CharField(max_length=255, blank=True, null=True)
    sell_point = models.CharField(max_length=255, blank=True, null=True)
    product_describe = models.CharField(max_length=255, blank=True, null=True)
    share_title = models.CharField(max_length=255, blank=True, null=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reduced_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    pay_limit = models.IntegerField(blank=True, null=True)
    parter_number = models.IntegerField(blank=True, null=True)
    group_upper_limit = models.IntegerField(blank=True, null=True)
    join_upper_limit = models.IntegerField(blank=True, null=True)
    hotsale_falg = models.IntegerField(db_column='HotSale_falg', blank=True, null=True)  # Field name made lowercase.
    sort_id = models.IntegerField(db_column='sort_Id', blank=True, null=True)  # Field name made lowercase.
    ship_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    discountamount = models.DecimalField(db_column='discountAmount', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'o_hotsale'


class OPaintedEggAct(models.Model):
    activity_name = models.CharField(max_length=50, blank=True, null=True)
    vouche_prefix = models.CharField(max_length=30)
    vouche_start_pos = models.CharField(max_length=30)
    total_vouche = models.IntegerField()
    insert_by = models.IntegerField(blank=True, null=True)
    insert_timestamp = models.DateTimeField(blank=True, null=True)
    update_by = models.IntegerField(blank=True, null=True)
    update_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_painted_egg_act'


class OPavilion(models.Model):
    pid = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    pav_name = models.CharField(db_column='PAV_NAME', max_length=64)  # Field name made lowercase.
    pavilion_code = models.CharField(db_column='PAVILION_CODE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    banner_pic = models.CharField(db_column='BANNER_PIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    top_pic = models.CharField(db_column='TOP_PIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    share_pic = models.CharField(db_column='SHARE_PIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    begin_time = models.DateTimeField(db_column='BEGIN_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insert_timestamp = models.DateTimeField(db_column='INSERT_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    insert_by = models.IntegerField(db_column='INSERT_BY', blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey(DPavStatus, models.DO_NOTHING, db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='UPDATE_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.IntegerField(db_column='UPDATED_BY', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.
    context_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_pavilion'


class Offlinecart(models.Model):
    offlinecartid = models.BigAutoField(db_column='id', primary_key=True)
    devicenumber = models.CharField(db_column='deviceNumber', max_length=50)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=60)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=120)  # Field name made lowercase.
    goodstitle = models.CharField(db_column='goodsTitle', max_length=120)  # Field name made lowercase.
    cnt = models.PositiveSmallIntegerField()
    extensioncode = models.CharField(db_column='extensionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isgift = models.PositiveIntegerField(db_column='isGift')  # Field name made lowercase.
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    tagids = models.CharField(db_column='tagIds', max_length=120, blank=True, null=True)  # Field name made lowercase.
    goodsattrids = models.CharField(db_column='goodsAttrIds', max_length=120)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64)  # Field name made lowercase.
    ischeck = models.TextField(blank=True, null=True)  # This field type is a guess.
    packageid = models.IntegerField(db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    packagegroupid = models.IntegerField(db_column='packageGroupId', blank=True, null=True)  # Field name made lowercase.
    packageindex = models.IntegerField(db_column='packageIndex', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'offlinecart'


class Offlinerefundorderslog(models.Model):
    refundlogid = models.AutoField(db_column='refundlogId', primary_key=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    complaintstype = models.IntegerField(db_column='complaintsType', blank=True, null=True)  # Field name made lowercase.
    reason = models.IntegerField(blank=True, null=True)
    amountreceived = models.DecimalField(db_column='amountReceived', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountrefund = models.DecimalField(db_column='amountRefund', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundchannel = models.IntegerField(db_column='refundChannel', blank=True, null=True)  # Field name made lowercase.
    otherpartyaccount = models.CharField(db_column='otherPartyAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    refundchanneldesc = models.CharField(db_column='refundChannelDesc', max_length=128, blank=True, null=True)  # Field name made lowercase.
    creater = models.CharField(max_length=64, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True, default=datetime.date.today)  # Field name made lowercase.
    aftersaletypeid = models.IntegerField(db_column='aftersaletypeid', blank=True, null=True)
    source = models.IntegerField(db_column='source', blank=True, null=True)
    isreship = models.IntegerField(db_column='isreship', blank=True, null=True)
    isrefund = models.IntegerField(db_column='isrefund', blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    result = models.CharField(max_length=2048, blank=True, null=True)
    imgages = models.CharField(max_length=2048, blank=True, null=True)
    status = models.IntegerField(db_column='status', blank=True, null=True)
    deptsid = models.IntegerField(db_column='deptsId', blank=True, null=True)  # Field name made lowercase.
    deptsname = models.CharField(db_column='deptsName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        import datetime, decimal
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), decimal.Decimal):
                d[attr] = getattr(self, attr, 0.00)
            else:
                d[attr] = getattr(self, attr)

        #import json
        return d

    class Meta:
        managed = False
        db_table = 'offlinerefundorderslog'


class Offlinerefundorderslogdetail(models.Model):
    refundlogid = models.IntegerField(db_column='refundlogId', blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=32, blank=True, null=True)  # Field name made lowercase.
    goodsid = models.CharField(db_column='goodsId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    realprice = models.DecimalField(db_column='realPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    realintegral = models.DecimalField(db_column='realIntegral', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    paidsubtotal = models.DecimalField(db_column='paidSubtotal', max_digits=10, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        import datetime, decimal
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), decimal.Decimal):
                d[attr] = getattr(self, attr, 0.00)
            else:
                d[attr] = getattr(self, attr)

        #import json
        return d

    class Meta:
        managed = False
        db_table = 'offlinerefundorderslogdetail'


class OrderCreationLog(models.Model):
    goodsamount = models.DecimalField(db_column='goodsAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    integral = models.IntegerField(blank=True, null=True)
    vouchermoney = models.DecimalField(db_column='voucherMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vouchercodemoney = models.DecimalField(db_column='voucherCodeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    voucherids = models.CharField(db_column='voucherIds', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.CharField(db_column='voucherCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    needtopay = models.DecimalField(db_column='needToPay', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=30, blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_creation_log'


class OrderDistributionRemark(models.Model):
    ordersn = models.CharField(db_column='orderSn', max_length=20)  # Field name made lowercase.
    content = models.CharField(max_length=200, blank=True, null=True)
    remarktypes = models.CharField(db_column='remarkTypes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    distributor = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    imageurl = models.CharField(db_column='imageUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    submittime = models.DateTimeField(db_column='submitTime', blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_distribution_remark'
        unique_together = (('id', 'ordersn'),)


class Orderaction(models.Model):
    orderactionid = models.BigAutoField(db_column='id',primary_key=True)
    orderid = models.PositiveIntegerField(db_column='orderId')  # Field name made lowercase.
    operatorid = models.CharField(db_column='operatorId', max_length=30)  # Field name made lowercase.
    statustype = models.PositiveIntegerField(db_column='statusType')  # Field name made lowercase.
    orginalstatus = models.PositiveIntegerField(db_column='orginalStatus')  # Field name made lowercase.
    currentstatus = models.PositiveIntegerField(db_column='currentStatus')  # Field name made lowercase.
    note = models.CharField(max_length=255)
    logtime = models.PositiveIntegerField(db_column='logTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderaction'


class Orderdeliverypowerlimit(models.Model):
    dayofweek = models.IntegerField(db_column='dayOfWeek')  # Field name made lowercase.
    deliverytimeid = models.IntegerField(db_column='deliveryTimeId')  # Field name made lowercase.
    orderamountlimit = models.DecimalField(db_column='orderAmountLimit', max_digits=10, decimal_places=2)  # Field name made lowercase.
    deliverypowerlimit = models.IntegerField(db_column='deliveryPowerLimit')  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime')  # Field name made lowercase.
    creator = models.CharField(max_length=255)
    updater = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderdeliverypowerlimit'


class Orderdetail(models.Model):
    orderid = models.PositiveIntegerField(db_column='orderId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=60)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=120)  # Field name made lowercase.
    goodstitle = models.CharField(db_column='goodsTitle', max_length=120)  # Field name made lowercase.
    cnt = models.PositiveSmallIntegerField()
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    realprice = models.DecimalField(db_column='realPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    realintegral = models.DecimalField(db_column='realIntegral', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    extensioncode = models.CharField(max_length=30, blank=True, null=True)
    isgift = models.PositiveIntegerField(db_column='isGift')  # Field name made lowercase.
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    tagids = models.CharField(db_column='tagIds', max_length=120, blank=True, null=True)  # Field name made lowercase.
    goodsattrids = models.CharField(db_column='goodsAttrIds', max_length=120)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    user_id_old = models.IntegerField(blank=True, null=True)
    rec_id_old = models.IntegerField(blank=True, null=True)
    paidsubtotal = models.DecimalField(db_column='paidSubtotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isgroupgoods = models.IntegerField(db_column='isGroupGoods', blank=True, null=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    packagegroupid = models.IntegerField(db_column='packageGroupId', blank=True, null=True)  # Field name made lowercase.
    packageindex = models.IntegerField(db_column='packageIndex', blank=True, null=True)  # Field name made lowercase.
    supackageid = models.IntegerField(db_column='supackageId', blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        import datetime, decimal
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), decimal.Decimal):
                d[attr] = getattr(self, attr, 0.00)
            else:
                d[attr] = getattr(self, attr)
        return d

    class Meta:
        managed = False
        db_table = 'orderdetail'


class OrderdetailCopy(models.Model):
    orderid = models.PositiveIntegerField(db_column='orderId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=60)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=120)  # Field name made lowercase.
    goodstitle = models.CharField(db_column='goodsTitle', max_length=120)  # Field name made lowercase.
    cnt = models.PositiveSmallIntegerField()
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    realprice = models.DecimalField(db_column='realPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    realintegral = models.DecimalField(db_column='realIntegral', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    extensioncode = models.CharField(max_length=30, blank=True, null=True)
    isgift = models.PositiveIntegerField(db_column='isGift')  # Field name made lowercase.
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    tagids = models.CharField(db_column='tagIds', max_length=120, blank=True, null=True)  # Field name made lowercase.
    goodsattrids = models.CharField(db_column='goodsAttrIds', max_length=120)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    user_id_old = models.IntegerField(blank=True, null=True)
    rec_id_old = models.IntegerField(blank=True, null=True)
    paidsubtotal = models.DecimalField(db_column='paidSubtotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isgroupgoods = models.IntegerField(db_column='isGroupGoods', blank=True, null=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    packagegroupid = models.IntegerField(db_column='packageGroupId', blank=True, null=True)  # Field name made lowercase.
    packageindex = models.IntegerField(db_column='packageIndex', blank=True, null=True)  # Field name made lowercase.
    supackageid = models.IntegerField(db_column='supackageId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetail_copy'


class OrderdetailHistory(models.Model):
    orderdetailhistoryid = models.PositiveIntegerField(db_column='id',primary_key=True)
    orderid = models.PositiveIntegerField(db_column='orderId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=60)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=120)  # Field name made lowercase.
    goodstitle = models.CharField(db_column='goodsTitle', max_length=120)  # Field name made lowercase.
    cnt = models.PositiveSmallIntegerField()
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    realprice = models.DecimalField(db_column='realPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    realintegral = models.DecimalField(db_column='realIntegral', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    extensioncode = models.CharField(max_length=30, blank=True, null=True)
    isgift = models.PositiveIntegerField(db_column='isGift')  # Field name made lowercase.
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    tagids = models.CharField(db_column='tagIds', max_length=120, blank=True, null=True)  # Field name made lowercase.
    goodsattrids = models.CharField(db_column='goodsAttrIds', max_length=120)  # Field name made lowercase.
    parentguid = models.CharField(db_column='parentGuid', max_length=64)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    user_id_old = models.IntegerField(blank=True, null=True)
    rec_id_old = models.IntegerField(blank=True, null=True)
    paidsubtotal = models.DecimalField(db_column='paidSubtotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isgroupgoods = models.IntegerField(db_column='isGroupGoods', blank=True, null=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    packagegroupid = models.IntegerField(db_column='packageGroupId', blank=True, null=True)  # Field name made lowercase.
    packageindex = models.IntegerField(db_column='packageIndex', blank=True, null=True)  # Field name made lowercase.
    supackageid = models.IntegerField(db_column='supackageId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetail_history'


class Orderdetailsupackage(models.Model):
    orderid = models.PositiveIntegerField(db_column='orderId')  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=60)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=120)  # Field name made lowercase.
    goodstitle = models.CharField(db_column='goodsTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cnt = models.PositiveSmallIntegerField()
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    realprice = models.DecimalField(db_column='realPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    realintegral = models.DecimalField(db_column='realIntegral', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    isgift = models.PositiveIntegerField(db_column='isGift')  # Field name made lowercase.
    paidsubtotal = models.DecimalField(db_column='paidSubtotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isgroupgoods = models.IntegerField(db_column='isGroupGoods', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetailsupackage'


class Orderexception(models.Model):
    code = models.CharField(max_length=4000)
    orderid = models.IntegerField(db_column='orderId')  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdBy')  # Field name made lowercase.
    description = models.CharField(max_length=255)
    handledby = models.IntegerField(db_column='handledBy', blank=True, null=True)  # Field name made lowercase.
    handledtime = models.IntegerField(db_column='handledTime', blank=True, null=True)  # Field name made lowercase.
    handledcomment = models.CharField(db_column='handledComment', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderexception'


class Orderexceptiontype(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    createdtime = models.IntegerField(db_column='createdTime')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdBy')  # Field name made lowercase.
    modifiedtime = models.IntegerField(db_column='modifiedTime', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.IntegerField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderexceptiontype'


class Orderinvoiceinfo(models.Model):
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=128, blank=True, null=True)
    invoicetype = models.IntegerField(db_column='invoiceType', blank=True, null=True)  # Field name made lowercase.
    invoiceform = models.IntegerField(db_column='invoiceForm', blank=True, null=True)  # Field name made lowercase.
    invoicetitle = models.CharField(db_column='invoiceTitle', max_length=128, blank=True, null=True)  # Field name made lowercase.
    taxidentificationnum = models.CharField(db_column='taxIdentificationNum', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderinvoiceinfo'


class Orderinvoicerecords(models.Model):
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    invoiceid = models.CharField(db_column='invoiceId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    invoicetype = models.IntegerField(db_column='invoiceType', blank=True, null=True)  # Field name made lowercase.
    invoiceform = models.IntegerField(db_column='invoiceForm', blank=True, null=True)  # Field name made lowercase.
    invoicecode = models.CharField(db_column='invoiceCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='invoiceNumber', max_length=16, blank=True, null=True)  # Field name made lowercase.
    invoiceoperationtype = models.IntegerField(db_column='invoiceOperationType', blank=True, null=True)  # Field name made lowercase.
    amountexcludingtax = models.DecimalField(db_column='amountExcludingTax', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxamount = models.DecimalField(db_column='taxAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    actiontype = models.IntegerField(db_column='actionType', blank=True, null=True)  # Field name made lowercase.
    invoicetime = models.IntegerField(db_column='invoiceTime', blank=True, null=True)  # Field name made lowercase.
    invoiceurl = models.CharField(db_column='invoiceUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    invoicestatus = models.IntegerField(db_column='invoiceStatus', blank=True, null=True)  # Field name made lowercase.
    resultcode = models.CharField(db_column='resultCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    resultdescription = models.CharField(db_column='resultDescription', max_length=128, blank=True, null=True)  # Field name made lowercase.
    resultdata = models.CharField(db_column='resultData', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=32, blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        import datetime, decimal
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), decimal.Decimal):
                d[attr] = getattr(self, attr, 0.00)
            else:
                d[attr] = getattr(self, attr)
        return d

    class Meta:
        managed = False
        db_table = 'orderinvoicerecords'


class Orderpromotion(models.Model):
    orderid = models.AutoField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    promotiontype = models.PositiveIntegerField(db_column='promotionType')  # Field name made lowercase.
    promotionid = models.PositiveIntegerField(db_column='promotionId')  # Field name made lowercase.
    promotiondesc = models.CharField(db_column='promotionDesc', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    goodsguids = models.CharField(db_column='goodsGuids', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderpromotion'


class Orderrefund(models.Model):
    ordersn = models.CharField(db_column='orderSn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memberaccount = models.CharField(db_column='memberAccount', max_length=60, blank=True, null=True)  # Field name made lowercase.
    payid = models.PositiveIntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tradeno = models.CharField(db_column='tradeNo', max_length=256, blank=True, null=True)  # Field name made lowercase.
    queryid = models.CharField(db_column='queryId', max_length=256, blank=True, null=True)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    integralmoney = models.DecimalField(db_column='integralMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundamount = models.DecimalField(db_column='refundAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paystatus = models.PositiveIntegerField(db_column='payStatus', blank=True, null=True)  # Field name made lowercase.
    ordercreatetime = models.CharField(db_column='orderCreateTime', max_length=14, blank=True, null=True)  # Field name made lowercase.
    handlestatus = models.PositiveIntegerField(db_column='handleStatus', blank=True, null=True)  # Field name made lowercase.
    handleremark = models.CharField(db_column='handleRemark', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    bankrefundstatus = models.PositiveIntegerField(db_column='bankRefundStatus', blank=True, null=True)  # Field name made lowercase.
    bankrefundmsg = models.CharField(db_column='bankRefundMsg', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    creationtime = models.PositiveIntegerField(db_column='creationTime', blank=True, null=True)  # Field name made lowercase.
    creatoruserid = models.CharField(db_column='creatorUserId', max_length=60, blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.PositiveIntegerField(db_column='lastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.CharField(db_column='lastModifierUserId', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderrefund'


class Orders(models.Model):
    orderid = models.AutoField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', unique=True, max_length=20)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    ordertype = models.PositiveIntegerField(db_column='orderType')  # Field name made lowercase.
    orderstatus = models.PositiveIntegerField(db_column='orderStatus')  # Field name made lowercase.
    shippingstatus = models.PositiveIntegerField(db_column='shippingStatus')  # Field name made lowercase.
    paystatus = models.PositiveIntegerField(db_column='payStatus')  # Field name made lowercase.
    exceptionstatus = models.PositiveIntegerField(db_column='exceptionStatus')  # Field name made lowercase.
    deliverystatus = models.PositiveIntegerField(db_column='deliveryStatus')  # Field name made lowercase.
    consignee = models.CharField(max_length=64)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    sitesn = models.CharField(db_column='siteSN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    deliverytimebegin = models.PositiveIntegerField(db_column='deliveryTimeBegin')  # Field name made lowercase.
    deliverytimeend = models.PositiveIntegerField(db_column='deliveryTimeEnd')  # Field name made lowercase.
    postscript = models.CharField(db_column='postScript', max_length=255, blank=True, null=True)  # Field name made lowercase.
    messagetobuyer = models.CharField(db_column='messageToBuyer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingid = models.PositiveIntegerField(db_column='shippingId')  # Field name made lowercase.
    shippingname = models.CharField(db_column='shippingName', max_length=120)  # Field name made lowercase.
    payid = models.PositiveIntegerField(db_column='payId')  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120)  # Field name made lowercase.
    paynote = models.CharField(db_column='payNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    howoos = models.CharField(db_column='howOos', max_length=120)  # Field name made lowercase.
    howsurplus = models.CharField(db_column='howSurplus', max_length=120)  # Field name made lowercase.
    packname = models.CharField(db_column='packName', max_length=120)  # Field name made lowercase.
    invpayee = models.CharField(db_column='invPayee', max_length=120, blank=True, null=True)  # Field name made lowercase.
    invtype = models.CharField(db_column='invType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    invcontent = models.CharField(db_column='invContent', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goodsamount = models.DecimalField(db_column='goodsAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    insurefee = models.DecimalField(db_column='insureFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payfee = models.DecimalField(db_column='payFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    packfee = models.DecimalField(db_column='packFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2)  # Field name made lowercase.
    surplus = models.DecimalField(max_digits=10, decimal_places=2)
    integral = models.DecimalField(max_digits=10, decimal_places=0)
    integralmoney = models.DecimalField(db_column='integralMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    voucher = models.DecimalField(max_digits=10, decimal_places=2)
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime')  # Field name made lowercase.
    confirmtime = models.PositiveIntegerField(db_column='confirmTime', blank=True, null=True)  # Field name made lowercase.
    paytime = models.PositiveIntegerField(db_column='payTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.PositiveIntegerField(db_column='shippingTime', blank=True, null=True)  # Field name made lowercase.
    receivetime = models.PositiveIntegerField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    closetime = models.PositiveIntegerField(db_column='closeTime', blank=True, null=True)  # Field name made lowercase.
    packid = models.PositiveSmallIntegerField(db_column='packId', blank=True, null=True)  # Field name made lowercase.
    voucherids = models.CharField(db_column='voucherIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=255)  # Field name made lowercase.
    extensioncode = models.CharField(db_column='extensionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='printTimes', blank=True, null=True)  # Field name made lowercase.
    printusernames = models.CharField(db_column='printUserNames', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vouchermoney = models.DecimalField(db_column='voucherMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    needtopay = models.DecimalField(db_column='needToPay', max_digits=10, decimal_places=2)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    vouchercodemoney = models.DecimalField(db_column='voucherCodeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.CharField(db_column='voucherCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    deliverystatuschangedate = models.IntegerField(blank=True, null=True)
    freeshippingvoucheramount = models.DecimalField(db_column='freeShippingVoucherAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    canrestoreorder = models.IntegerField(db_column='canRestoreOrder')  # Field name made lowercase.
    originaldeliverytimebegin = models.IntegerField(db_column='originalDeliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    originaldeliverytimeend = models.IntegerField(db_column='originalDeliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    originalregion = models.CharField(db_column='originalRegion', max_length=32, blank=True, null=True)  # Field name made lowercase.
    originaladdress = models.CharField(db_column='originalAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    restoreorderid = models.IntegerField(db_column='restoreOrderId', blank=True, null=True)  # Field name made lowercase.
    iscancel = models.TextField(db_column='isCancel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cancelid = models.IntegerField(db_column='cancelId', blank=True, null=True)  # Field name made lowercase.
    ischangeshippingtime = models.IntegerField(db_column='isChangeShippingTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    rechargepromocode = models.CharField(db_column='rechargePromoCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=200, blank=True, null=True)
    customserviceremark = models.CharField(db_column='customServiceRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    baogangscore = models.DecimalField(db_column='baogangScore', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    streetnumber = models.CharField(db_column='streetNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cancelordernoticewx = models.IntegerField(db_column='cancelOrderNoticeWX', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.IntegerField(blank=True, null=True)
    taxidentificationnum = models.CharField(db_column='taxIdentificationNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    externaldiscount = models.FloatField(db_column='externalDiscount')  # Field name made lowercase.
    appversion = models.CharField(db_column='appVersion', max_length=16, blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        import datetime, decimal
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), decimal.Decimal):
                d[attr] = getattr(self, attr, 0.00)
            else:
                d[attr] = getattr(self, attr)

        #import json
        return d

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersActivity(models.Model):
    ordersn = models.CharField(db_column='orderSn', primary_key=True, max_length=255)  # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityId')  # Field name made lowercase.
    account = models.CharField(max_length=64)
    createdtime = models.DateTimeField(db_column='createdTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders_activity'


class OrdersCopy(models.Model):
    orderid = models.AutoField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', unique=True, max_length=20)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    ordertype = models.PositiveIntegerField(db_column='orderType')  # Field name made lowercase.
    orderstatus = models.PositiveIntegerField(db_column='orderStatus')  # Field name made lowercase.
    shippingstatus = models.PositiveIntegerField(db_column='shippingStatus')  # Field name made lowercase.
    paystatus = models.PositiveIntegerField(db_column='payStatus')  # Field name made lowercase.
    exceptionstatus = models.PositiveIntegerField(db_column='exceptionStatus')  # Field name made lowercase.
    deliverystatus = models.PositiveIntegerField(db_column='deliveryStatus')  # Field name made lowercase.
    consignee = models.CharField(max_length=64)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    sitesn = models.CharField(db_column='siteSN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    deliverytimebegin = models.PositiveIntegerField(db_column='deliveryTimeBegin')  # Field name made lowercase.
    deliverytimeend = models.PositiveIntegerField(db_column='deliveryTimeEnd')  # Field name made lowercase.
    postscript = models.CharField(db_column='postScript', max_length=255, blank=True, null=True)  # Field name made lowercase.
    messagetobuyer = models.CharField(db_column='messageToBuyer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingid = models.PositiveIntegerField(db_column='shippingId')  # Field name made lowercase.
    shippingname = models.CharField(db_column='shippingName', max_length=120)  # Field name made lowercase.
    payid = models.PositiveIntegerField(db_column='payId')  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120)  # Field name made lowercase.
    paynote = models.CharField(db_column='payNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    howoos = models.CharField(db_column='howOos', max_length=120)  # Field name made lowercase.
    howsurplus = models.CharField(db_column='howSurplus', max_length=120)  # Field name made lowercase.
    packname = models.CharField(db_column='packName', max_length=120)  # Field name made lowercase.
    invpayee = models.CharField(db_column='invPayee', max_length=120, blank=True, null=True)  # Field name made lowercase.
    invtype = models.CharField(db_column='invType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    invcontent = models.CharField(db_column='invContent', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goodsamount = models.DecimalField(db_column='goodsAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    insurefee = models.DecimalField(db_column='insureFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payfee = models.DecimalField(db_column='payFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    packfee = models.DecimalField(db_column='packFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2)  # Field name made lowercase.
    surplus = models.DecimalField(max_digits=10, decimal_places=2)
    integral = models.DecimalField(max_digits=10, decimal_places=0)
    integralmoney = models.DecimalField(db_column='integralMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    voucher = models.DecimalField(max_digits=10, decimal_places=2)
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime')  # Field name made lowercase.
    confirmtime = models.PositiveIntegerField(db_column='confirmTime', blank=True, null=True)  # Field name made lowercase.
    paytime = models.PositiveIntegerField(db_column='payTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.PositiveIntegerField(db_column='shippingTime', blank=True, null=True)  # Field name made lowercase.
    receivetime = models.PositiveIntegerField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    closetime = models.PositiveIntegerField(db_column='closeTime', blank=True, null=True)  # Field name made lowercase.
    packid = models.PositiveSmallIntegerField(db_column='packId', blank=True, null=True)  # Field name made lowercase.
    voucherids = models.CharField(db_column='voucherIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=255)  # Field name made lowercase.
    extensioncode = models.CharField(db_column='extensionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='printTimes', blank=True, null=True)  # Field name made lowercase.
    printusernames = models.CharField(db_column='printUserNames', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vouchermoney = models.DecimalField(db_column='voucherMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    needtopay = models.DecimalField(db_column='needToPay', max_digits=10, decimal_places=2)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    vouchercodemoney = models.DecimalField(db_column='voucherCodeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.CharField(db_column='voucherCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    deliverystatuschangedate = models.IntegerField(blank=True, null=True)
    freeshippingvoucheramount = models.DecimalField(db_column='freeShippingVoucherAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    canrestoreorder = models.IntegerField(db_column='canRestoreOrder')  # Field name made lowercase.
    originaldeliverytimebegin = models.IntegerField(db_column='originalDeliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    originaldeliverytimeend = models.IntegerField(db_column='originalDeliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    originalregion = models.CharField(db_column='originalRegion', max_length=32, blank=True, null=True)  # Field name made lowercase.
    originaladdress = models.CharField(db_column='originalAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    restoreorderid = models.IntegerField(db_column='restoreOrderId', blank=True, null=True)  # Field name made lowercase.
    iscancel = models.TextField(db_column='isCancel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cancelid = models.IntegerField(db_column='cancelId', blank=True, null=True)  # Field name made lowercase.
    ischangeshippingtime = models.IntegerField(db_column='isChangeShippingTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    rechargepromocode = models.CharField(db_column='rechargePromoCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=200, blank=True, null=True)
    customserviceremark = models.CharField(db_column='customServiceRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    baogangscore = models.DecimalField(db_column='baogangScore', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    streetnumber = models.CharField(db_column='streetNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cancelordernoticewx = models.IntegerField(db_column='cancelOrderNoticeWX', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.IntegerField(blank=True, null=True)
    taxidentificationnum = models.CharField(db_column='taxIdentificationNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    externaldiscount = models.FloatField(db_column='externalDiscount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders_copy'


class OrdersCopy1(models.Model):
    orderid = models.AutoField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', unique=True, max_length=20)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    ordertype = models.PositiveIntegerField(db_column='orderType')  # Field name made lowercase.
    orderstatus = models.PositiveIntegerField(db_column='orderStatus')  # Field name made lowercase.
    shippingstatus = models.PositiveIntegerField(db_column='shippingStatus')  # Field name made lowercase.
    paystatus = models.PositiveIntegerField(db_column='payStatus')  # Field name made lowercase.
    exceptionstatus = models.PositiveIntegerField(db_column='exceptionStatus')  # Field name made lowercase.
    deliverystatus = models.PositiveIntegerField(db_column='deliveryStatus')  # Field name made lowercase.
    consignee = models.CharField(max_length=64)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    sitesn = models.CharField(db_column='siteSN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    deliverytimebegin = models.PositiveIntegerField(db_column='deliveryTimeBegin')  # Field name made lowercase.
    deliverytimeend = models.PositiveIntegerField(db_column='deliveryTimeEnd')  # Field name made lowercase.
    postscript = models.CharField(db_column='postScript', max_length=255, blank=True, null=True)  # Field name made lowercase.
    messagetobuyer = models.CharField(db_column='messageToBuyer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingid = models.PositiveIntegerField(db_column='shippingId')  # Field name made lowercase.
    shippingname = models.CharField(db_column='shippingName', max_length=120)  # Field name made lowercase.
    payid = models.PositiveIntegerField(db_column='payId')  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120)  # Field name made lowercase.
    paynote = models.CharField(db_column='payNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    howoos = models.CharField(db_column='howOos', max_length=120)  # Field name made lowercase.
    howsurplus = models.CharField(db_column='howSurplus', max_length=120)  # Field name made lowercase.
    packname = models.CharField(db_column='packName', max_length=120)  # Field name made lowercase.
    invpayee = models.CharField(db_column='invPayee', max_length=120, blank=True, null=True)  # Field name made lowercase.
    invtype = models.CharField(db_column='invType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    invcontent = models.CharField(db_column='invContent', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goodsamount = models.DecimalField(db_column='goodsAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    insurefee = models.DecimalField(db_column='insureFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payfee = models.DecimalField(db_column='payFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    packfee = models.DecimalField(db_column='packFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2)  # Field name made lowercase.
    surplus = models.DecimalField(max_digits=10, decimal_places=2)
    integral = models.DecimalField(max_digits=10, decimal_places=0)
    integralmoney = models.DecimalField(db_column='integralMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    voucher = models.DecimalField(max_digits=10, decimal_places=2)
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime')  # Field name made lowercase.
    confirmtime = models.PositiveIntegerField(db_column='confirmTime', blank=True, null=True)  # Field name made lowercase.
    paytime = models.PositiveIntegerField(db_column='payTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.PositiveIntegerField(db_column='shippingTime', blank=True, null=True)  # Field name made lowercase.
    receivetime = models.PositiveIntegerField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    closetime = models.PositiveIntegerField(db_column='closeTime', blank=True, null=True)  # Field name made lowercase.
    packid = models.PositiveSmallIntegerField(db_column='packId', blank=True, null=True)  # Field name made lowercase.
    voucherids = models.CharField(db_column='voucherIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=255)  # Field name made lowercase.
    extensioncode = models.CharField(db_column='extensionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='printTimes', blank=True, null=True)  # Field name made lowercase.
    printusernames = models.CharField(db_column='printUserNames', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vouchermoney = models.DecimalField(db_column='voucherMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    needtopay = models.DecimalField(db_column='needToPay', max_digits=10, decimal_places=2)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    vouchercodemoney = models.DecimalField(db_column='voucherCodeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.CharField(db_column='voucherCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    deliverystatuschangedate = models.IntegerField(blank=True, null=True)
    freeshippingvoucheramount = models.DecimalField(db_column='freeShippingVoucherAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    canrestoreorder = models.IntegerField(db_column='canRestoreOrder')  # Field name made lowercase.
    originaldeliverytimebegin = models.IntegerField(db_column='originalDeliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    originaldeliverytimeend = models.IntegerField(db_column='originalDeliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    originalregion = models.CharField(db_column='originalRegion', max_length=32, blank=True, null=True)  # Field name made lowercase.
    originaladdress = models.CharField(db_column='originalAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    restoreorderid = models.IntegerField(db_column='restoreOrderId', blank=True, null=True)  # Field name made lowercase.
    iscancel = models.TextField(db_column='isCancel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cancelid = models.IntegerField(db_column='cancelId', blank=True, null=True)  # Field name made lowercase.
    ischangeshippingtime = models.IntegerField(db_column='isChangeShippingTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    rechargepromocode = models.CharField(db_column='rechargePromoCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=200, blank=True, null=True)
    customserviceremark = models.CharField(db_column='customServiceRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    baogangscore = models.DecimalField(db_column='baogangScore', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    streetnumber = models.CharField(db_column='streetNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cancelordernoticewx = models.IntegerField(db_column='cancelOrderNoticeWX', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.IntegerField(blank=True, null=True)
    taxidentificationnum = models.CharField(db_column='taxIdentificationNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    externaldiscount = models.FloatField(db_column='externalDiscount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders_copy1'


class OrdersHistory(models.Model):
    orderid = models.PositiveIntegerField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=20)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    ordertype = models.PositiveIntegerField(db_column='orderType')  # Field name made lowercase.
    orderstatus = models.PositiveIntegerField(db_column='orderStatus')  # Field name made lowercase.
    shippingstatus = models.PositiveIntegerField(db_column='shippingStatus')  # Field name made lowercase.
    paystatus = models.PositiveIntegerField(db_column='payStatus')  # Field name made lowercase.
    exceptionstatus = models.PositiveIntegerField(db_column='exceptionStatus')  # Field name made lowercase.
    deliverystatus = models.PositiveIntegerField(db_column='deliveryStatus')  # Field name made lowercase.
    consignee = models.CharField(max_length=64)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    sitesn = models.CharField(db_column='siteSN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    deliverytimebegin = models.PositiveIntegerField(db_column='deliveryTimeBegin')  # Field name made lowercase.
    deliverytimeend = models.PositiveIntegerField(db_column='deliveryTimeEnd')  # Field name made lowercase.
    postscript = models.CharField(db_column='postScript', max_length=255, blank=True, null=True)  # Field name made lowercase.
    messagetobuyer = models.CharField(db_column='messageToBuyer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingid = models.PositiveIntegerField(db_column='shippingId')  # Field name made lowercase.
    shippingname = models.CharField(db_column='shippingName', max_length=120)  # Field name made lowercase.
    payid = models.PositiveIntegerField(db_column='payId')  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120)  # Field name made lowercase.
    paynote = models.CharField(db_column='payNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    howoos = models.CharField(db_column='howOos', max_length=120)  # Field name made lowercase.
    howsurplus = models.CharField(db_column='howSurplus', max_length=120)  # Field name made lowercase.
    packname = models.CharField(db_column='packName', max_length=120)  # Field name made lowercase.
    invpayee = models.CharField(db_column='invPayee', max_length=120, blank=True, null=True)  # Field name made lowercase.
    invtype = models.CharField(db_column='invType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    invcontent = models.CharField(db_column='invContent', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goodsamount = models.DecimalField(db_column='goodsAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    insurefee = models.DecimalField(db_column='insureFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payfee = models.DecimalField(db_column='payFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    packfee = models.DecimalField(db_column='packFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2)  # Field name made lowercase.
    surplus = models.DecimalField(max_digits=10, decimal_places=2)
    integral = models.DecimalField(max_digits=10, decimal_places=0)
    integralmoney = models.DecimalField(db_column='integralMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    voucher = models.DecimalField(max_digits=10, decimal_places=2)
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime')  # Field name made lowercase.
    confirmtime = models.PositiveIntegerField(db_column='confirmTime', blank=True, null=True)  # Field name made lowercase.
    paytime = models.PositiveIntegerField(db_column='payTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.PositiveIntegerField(db_column='shippingTime', blank=True, null=True)  # Field name made lowercase.
    receivetime = models.PositiveIntegerField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    closetime = models.PositiveIntegerField(db_column='closeTime', blank=True, null=True)  # Field name made lowercase.
    packid = models.PositiveSmallIntegerField(db_column='packId', blank=True, null=True)  # Field name made lowercase.
    voucherids = models.CharField(db_column='voucherIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=255)  # Field name made lowercase.
    extensioncode = models.CharField(db_column='extensionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='printTimes', blank=True, null=True)  # Field name made lowercase.
    printusernames = models.CharField(db_column='printUserNames', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vouchermoney = models.DecimalField(db_column='voucherMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    needtopay = models.DecimalField(db_column='needToPay', max_digits=10, decimal_places=2)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    vouchercodemoney = models.DecimalField(db_column='voucherCodeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.CharField(db_column='voucherCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)
    deliverystatuschangedate = models.IntegerField(blank=True, null=True)
    freeshippingvoucheramount = models.DecimalField(db_column='freeShippingVoucherAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    canrestoreorder = models.IntegerField(db_column='canRestoreOrder')  # Field name made lowercase.
    originaldeliverytimebegin = models.IntegerField(db_column='originalDeliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    originaldeliverytimeend = models.IntegerField(db_column='originalDeliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    originalregion = models.CharField(db_column='originalRegion', max_length=32, blank=True, null=True)  # Field name made lowercase.
    originaladdress = models.CharField(db_column='originalAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    restoreorderid = models.IntegerField(db_column='restoreOrderId', blank=True, null=True)  # Field name made lowercase.
    iscancel = models.TextField(db_column='isCancel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cancelid = models.IntegerField(db_column='cancelId', blank=True, null=True)  # Field name made lowercase.
    ischangeshippingtime = models.IntegerField(db_column='isChangeShippingTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    rechargepromocode = models.CharField(db_column='rechargePromoCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=200, blank=True, null=True)
    customserviceremark = models.CharField(db_column='customServiceRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    baogangscore = models.DecimalField(db_column='baogangScore', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    streetnumber = models.CharField(db_column='streetNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cancelordernoticewx = models.IntegerField(db_column='cancelOrderNoticeWX', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.IntegerField(blank=True, null=True)
    taxidentificationnum = models.CharField(db_column='taxIdentificationNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    externaldiscount = models.FloatField(db_column='externalDiscount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders_history'


class OrdersHistoryCount(models.Model):
    ordercount = models.IntegerField(db_column='orderCount', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders_history_count'


class OrdersPayno(models.Model):
    ordersn = models.CharField(db_column='orderSn', primary_key=True, max_length=20)  # Field name made lowercase.
    out_trade_no = models.CharField(max_length=32, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders_payno'


class OrdersPayremark(models.Model):
    ordersn = models.CharField(db_column='orderSn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders_payremark'


class OrdersUpdate(models.Model):
    orderid = models.PositiveIntegerField(db_column='orderId')  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=20)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    ordertype = models.PositiveIntegerField(db_column='orderType')  # Field name made lowercase.
    orderstatus = models.PositiveIntegerField(db_column='orderStatus')  # Field name made lowercase.
    shippingstatus = models.PositiveIntegerField(db_column='shippingStatus')  # Field name made lowercase.
    paystatus = models.PositiveIntegerField(db_column='payStatus')  # Field name made lowercase.
    exceptionstatus = models.PositiveIntegerField(db_column='exceptionStatus')  # Field name made lowercase.
    consignee = models.CharField(max_length=64)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    sitesn = models.CharField(db_column='siteSN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    deliverytimebegin = models.PositiveIntegerField(db_column='deliveryTimeBegin')  # Field name made lowercase.
    deliverytimeend = models.PositiveIntegerField(db_column='deliveryTimeEnd')  # Field name made lowercase.
    postscript = models.CharField(db_column='postScript', max_length=255, blank=True, null=True)  # Field name made lowercase.
    messagetobuyer = models.CharField(db_column='messageToBuyer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingid = models.PositiveIntegerField(db_column='shippingId')  # Field name made lowercase.
    shippingname = models.CharField(db_column='shippingName', max_length=120)  # Field name made lowercase.
    payid = models.PositiveIntegerField(db_column='payId')  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120)  # Field name made lowercase.
    paynote = models.CharField(db_column='payNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    howoos = models.CharField(db_column='howOos', max_length=120)  # Field name made lowercase.
    howsurplus = models.CharField(db_column='howSurplus', max_length=120)  # Field name made lowercase.
    packname = models.CharField(db_column='packName', max_length=120)  # Field name made lowercase.
    invpayee = models.CharField(db_column='invPayee', max_length=120, blank=True, null=True)  # Field name made lowercase.
    invtype = models.CharField(db_column='invType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    invcontent = models.CharField(db_column='invContent', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goodsamount = models.DecimalField(db_column='goodsAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    insurefee = models.DecimalField(db_column='insureFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payfee = models.DecimalField(db_column='payFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    packfee = models.DecimalField(db_column='packFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2)  # Field name made lowercase.
    surplus = models.DecimalField(max_digits=10, decimal_places=2)
    integral = models.DecimalField(max_digits=10, decimal_places=0)
    integralmoney = models.DecimalField(db_column='integralMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    voucher = models.DecimalField(max_digits=10, decimal_places=2)
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime')  # Field name made lowercase.
    confirmtime = models.PositiveIntegerField(db_column='confirmTime', blank=True, null=True)  # Field name made lowercase.
    paytime = models.PositiveIntegerField(db_column='payTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.PositiveIntegerField(db_column='shippingTime', blank=True, null=True)  # Field name made lowercase.
    receivetime = models.PositiveIntegerField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    closetime = models.PositiveIntegerField(db_column='closeTime', blank=True, null=True)  # Field name made lowercase.
    packid = models.PositiveSmallIntegerField(db_column='packId', blank=True, null=True)  # Field name made lowercase.
    voucherids = models.CharField(db_column='voucherIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=255)  # Field name made lowercase.
    extensioncode = models.CharField(db_column='extensionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='printTimes', blank=True, null=True)  # Field name made lowercase.
    printusernames = models.CharField(db_column='printUserNames', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vouchermoney = models.DecimalField(db_column='voucherMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.
    needtopay = models.DecimalField(db_column='needToPay', max_digits=10, decimal_places=2)  # Field name made lowercase.
    order_id_old = models.IntegerField(blank=True, null=True)
    vouchercodemoney = models.DecimalField(db_column='voucherCodeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    user_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_update'


class Ordersatisfy(models.Model):
    orderid = models.IntegerField(db_column='orderId')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    packagesatisfylevel = models.SmallIntegerField(db_column='packageSatisfyLevel', blank=True, null=True)  # Field name made lowercase.
    servicesatisfylevel = models.SmallIntegerField(db_column='serviceSatisfyLevel', blank=True, null=True)  # Field name made lowercase.
    logisticssatisfylevel = models.SmallIntegerField(db_column='logisticsSatisfyLevel', blank=True, null=True)  # Field name made lowercase.
    appsatisfylevel = models.SmallIntegerField(db_column='appSatisfyLevel', blank=True, null=True)  # Field name made lowercase.
    hasexamined = models.IntegerField(db_column='hasExamined', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordersatisfy'


class Ordersyncstatus(models.Model):
    orderid = models.CharField(db_column='orderId', max_length=64)  # Field name made lowercase.
    orderstatus = models.IntegerField(db_column='orderStatus')  # Field name made lowercase.
    paystatus = models.IntegerField(db_column='payStatus')  # Field name made lowercase.
    target = models.CharField(max_length=255, blank=True, null=True)
    apiname = models.CharField(db_column='apiName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderinfo = models.CharField(db_column='orderInfo', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    resultcode = models.IntegerField(db_column='resultCode', blank=True, null=True)  # Field name made lowercase.
    resultinfo = models.TextField(db_column='resultInfo', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordersyncstatus'


class Ordertypeamountnotice(models.Model):
    ordertype = models.PositiveIntegerField(db_column='orderType', blank=True, null=True)  # Field name made lowercase.
    orderamount = models.DecimalField(db_column='orderAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=256, blank=True, null=True)
    createat = models.DateTimeField(blank=True, null=True)
    createby = models.IntegerField(blank=True, null=True)
    updateat = models.DateTimeField(blank=True, null=True)
    updateby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordertypeamountnotice'


class Ordervoucher(models.Model):
    orderid = models.AutoField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    voucherid = models.PositiveIntegerField(db_column='voucherId')  # Field name made lowercase.
    vouchername = models.CharField(db_column='voucherName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    voucherdesc = models.CharField(db_column='voucherDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordervoucher'


class Packagegroup(models.Model):
    groupid = models.AutoField(db_column='groupId', primary_key=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='packageId')  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=100)  # Field name made lowercase.
    groupdesc = models.CharField(db_column='groupDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    goodscount = models.IntegerField(db_column='goodsCount', blank=True, null=True)  # Field name made lowercase.
    selectedcount = models.IntegerField(db_column='selectedCount', blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(blank=True, null=True)
    displayseq = models.IntegerField(db_column='displaySeq', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packagegroup'


class Packagegroupgoods(models.Model):
    groupgoodsid = models.AutoField(db_column='groupGoodsId', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupId', blank=True, null=True)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    display = models.IntegerField(blank=True, null=True)
    displayseq = models.IntegerField(db_column='displaySeq', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packagegroupgoods'


class Packageimages(models.Model):
    imageid = models.AutoField(db_column='imageId', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='pId', blank=True, null=True)  # Field name made lowercase.
    carouselimage = models.IntegerField(db_column='carouselImage', blank=True, null=True)  # Field name made lowercase.
    packagemainimage = models.IntegerField(db_column='packageMainImage', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=100, blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packageimages'


class Packageinfo(models.Model):
    pid = models.AutoField(db_column='pId', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='pName', max_length=100)  # Field name made lowercase.
    desc = models.CharField(max_length=200)
    materialnames = models.CharField(db_column='materialNames', max_length=300, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    groupdesc = models.CharField(db_column='groupDesc', max_length=300)  # Field name made lowercase.
    details = models.TextField(blank=True, null=True)
    sharetitle = models.CharField(db_column='shareTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sharecontent = models.CharField(db_column='shareContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shareicon = models.CharField(db_column='shareIcon', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField()
    displayseq = models.IntegerField(db_column='displaySeq', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packageinfo'


class Payerrorlog(models.Model):
    payerroelogid = models.BigAutoField(db_column='id',primary_key=True)
    ordersn = models.CharField(db_column='orderSn', max_length=60, blank=True, null=True)  # Field name made lowercase.
    errorcode = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    errorcontent = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payerrorlog'


class PayerrorlogHistory(models.Model):
    payerroeloghistoryid = models.IntegerField(db_column='id',primary_key=True)
    ordersn = models.CharField(db_column='orderSn', max_length=60, blank=True, null=True)  # Field name made lowercase.
    errorcode = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    errorcontent = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payerrorlog_history'


class Paypromotionrules(models.Model):
    rulename = models.CharField(db_column='ruleName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    payamount = models.DecimalField(db_column='payAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    minusamount = models.DecimalField(db_column='minusAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    daylimit = models.IntegerField(db_column='dayLimit', blank=True, null=True)  # Field name made lowercase.
    activitylimit = models.IntegerField(db_column='activityLimit', blank=True, null=True)  # Field name made lowercase.
    userdaylimit = models.IntegerField(db_column='userDayLimit', blank=True, null=True)  # Field name made lowercase.
    useractivitylimit = models.IntegerField(db_column='userActivityLimit', blank=True, null=True)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paypromotionrules'


class Paypromotionrulesorders(models.Model):
    payruleid = models.IntegerField(db_column='payRuleId', blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    originalamount = models.DecimalField(db_column='originalAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    actualamount = models.DecimalField(db_column='actualAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    minusamount = models.DecimalField(db_column='minusAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tradestatus = models.IntegerField(db_column='tradeStatus', blank=True, null=True)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='isEnable', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paypromotionrulesorders'


class Paysuccesslog(models.Model):
    paysuccesslogid = models.BigAutoField(db_column='id',primary_key=True)
    ordersn = models.CharField(db_column='orderSn', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ordersnextend = models.CharField(db_column='orderSnextend', max_length=60, blank=True, null=True)  # Field name made lowercase.
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(max_length=30, blank=True, null=True)
    trade_no = models.CharField(max_length=30, blank=True, null=True)
    trade_status = models.CharField(max_length=30, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_payment = models.DateTimeField(blank=True, null=True)
    buyer_account = models.CharField(max_length=100, blank=True, null=True)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    body = models.CharField(max_length=400, blank=True, null=True)
    requestdata = models.CharField(db_column='RequestData', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paysuccesslog'


class PaysuccesslogHistory(models.Model):
    paysuccessloghistoryid = models.IntegerField(db_column='id',primary_key=True)
    ordersn = models.CharField(db_column='orderSn', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ordersnextend = models.CharField(db_column='orderSnextend', max_length=60, blank=True, null=True)  # Field name made lowercase.
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(max_length=30, blank=True, null=True)
    trade_no = models.CharField(max_length=30, blank=True, null=True)
    trade_status = models.CharField(max_length=30, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_payment = models.DateTimeField(blank=True, null=True)
    buyer_account = models.CharField(max_length=100, blank=True, null=True)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    body = models.CharField(max_length=400, blank=True, null=True)
    requestdata = models.CharField(db_column='RequestData', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paysuccesslog_history'


class Paytype(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=120)
    fee = models.CharField(max_length=10)
    description = models.CharField(max_length=4000)
    order = models.IntegerField(blank=True, null=True)
    config = models.CharField(max_length=4000)
    enabled = models.PositiveIntegerField()
    ispaygoods = models.IntegerField(db_column='isPayGoods', blank=True, null=True)  # Field name made lowercase.
    ispayrule = models.IntegerField(db_column='isPayRule', blank=True, null=True)  # Field name made lowercase.
    isbacktrack = models.IntegerField(db_column='isBacktrack', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paytype'


class PlatformsgoodsWochugoods(models.Model):
    goodscode = models.CharField(max_length=50, blank=True, null=True)
    goodssku = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    goodsguid = models.CharField(db_column='goodsGuId', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'platformsgoods_wochugoods'


class Presaleinfo(models.Model):
    goodsguid = models.CharField(max_length=64)
    starttime = models.PositiveIntegerField(blank=True, null=True)
    endtime = models.PositiveIntegerField(blank=True, null=True)
    shippingfee = models.DecimalField(max_digits=10, decimal_places=2)
    shippingtype = models.IntegerField()
    shippingdate = models.PositiveIntegerField(blank=True, null=True)
    deadlinedate = models.PositiveIntegerField(blank=True, null=True)
    shippingstarthour = models.IntegerField(blank=True, null=True)
    shippingstartminute = models.IntegerField(blank=True, null=True)
    shippingendhour = models.IntegerField(blank=True, null=True)
    shippingendminute = models.IntegerField(blank=True, null=True)
    shippingdayofweek = models.CharField(max_length=64, blank=True, null=True)
    deadlinedayofweek = models.CharField(max_length=64, blank=True, null=True)
    deadlinedaytime = models.CharField(max_length=64, blank=True, null=True)
    createat = models.DateTimeField(blank=True, null=True)
    createby = models.IntegerField(blank=True, null=True)
    updateat = models.DateTimeField(blank=True, null=True)
    updateby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presaleinfo'


class Promotion(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    usercondition = models.CharField(db_column='userCondition', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    timecondition = models.CharField(db_column='timeCondition', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    addresscondition = models.CharField(db_column='addressCondition', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    orderdetailscondition = models.CharField(db_column='orderDetailsCondition', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ordercondition = models.CharField(db_column='orderCondition', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    paymentcondition = models.CharField(db_column='paymentCondition', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    parameters = models.CharField(max_length=1000, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    promotiontarget = models.CharField(db_column='promotionTarget', max_length=255, blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(blank=True, null=True)
    exclusion = models.IntegerField(blank=True, null=True)
    repeatable = models.TextField(blank=True, null=True)  # This field type is a guess.
    invalidated = models.TextField(blank=True, null=True)  # This field type is a guess.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    operationsequence = models.IntegerField(db_column='operationSequence', blank=True, null=True)  # Field name made lowercase.
    regulartype = models.IntegerField(db_column='regularType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotion'


class Promotionchannel(models.Model):
    weixinofficalaccount = models.CharField(db_column='weixinOfficalAccount', max_length=256)  # Field name made lowercase.
    channelname = models.CharField(db_column='channelName', max_length=256)  # Field name made lowercase.
    channelplan = models.CharField(db_column='channelPlan', max_length=256)  # Field name made lowercase.
    planname = models.CharField(db_column='planName', max_length=256)  # Field name made lowercase.
    planno = models.CharField(db_column='planNo', max_length=256)  # Field name made lowercase.
    url = models.CharField(max_length=512, blank=True, null=True)
    qrcodeurl = models.CharField(db_column='qrCodeUrl', max_length=512, blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='creationTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotionchannel'


class Promotiondiscount(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    promotiontype = models.IntegerField(db_column='promotionType', blank=True, null=True)  # Field name made lowercase.
    values = models.CharField(max_length=255, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    maxdiscount = models.DecimalField(db_column='maxDiscount', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ascendingmode = models.TextField(db_column='ascendingMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotiondiscount'


class Promotionflash(models.Model):
    title = models.CharField(max_length=55, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(max_length=32, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    purchaselimit = models.IntegerField(db_column='purchaseLimit', blank=True, null=True)  # Field name made lowercase.
    salednum = models.IntegerField(db_column='saledNum', blank=True, null=True)  # Field name made lowercase.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotionflash'


class Promotiongoodspay(models.Model):
    promotiongoodspayid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paytypeid = models.IntegerField(db_column='PayTypeId')  # Field name made lowercase.
    goodssn = models.CharField(db_column='GoodsSn', max_length=32)  # Field name made lowercase.
    promotiontype = models.IntegerField(db_column='PromotionType')  # Field name made lowercase.
    promotionvalue = models.CharField(db_column='PromotionValue', max_length=20, blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled')  # Field name made lowercase.
    lastoperatetime = models.DateTimeField(db_column='LastOperateTime')  # Field name made lowercase.
    lastoperator = models.CharField(db_column='LastOperator', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotiongoodspay'


class Promotiongrouppurchase(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)
    promotiontype = models.IntegerField(db_column='promotionType', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    minorders = models.IntegerField(db_column='minOrders', blank=True, null=True)  # Field name made lowercase.
    maxorders = models.IntegerField(db_column='maxOrders', blank=True, null=True)  # Field name made lowercase.
    repeatable = models.TextField(blank=True, null=True)  # This field type is a guess.
    shippingfee = models.DecimalField(db_column='shippingFee', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    closedtime = models.IntegerField(db_column='closedTime', blank=True, null=True)  # Field name made lowercase.
    successful = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotiongrouppurchase'


class Promotionorderspaychange(models.Model):
    promotionorderspaychangeid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='OrderSn', max_length=32)  # Field name made lowercase.
    paytypeid = models.IntegerField(db_column='PayTypeId')  # Field name made lowercase.
    moneypaidold = models.DecimalField(db_column='MoneyPaidOld', max_digits=8, decimal_places=2)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='MoneyPaid', max_digits=8, decimal_places=2)  # Field name made lowercase.
    needtopayold = models.DecimalField(db_column='NeedToPayOld', max_digits=8, decimal_places=2)  # Field name made lowercase.
    needtopay = models.DecimalField(db_column='NeedToPay', max_digits=8, decimal_places=2)  # Field name made lowercase.
    discountold = models.DecimalField(db_column='DiscountOld', max_digits=8, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=8, decimal_places=2)  # Field name made lowercase.
    shippingfeeold = models.DecimalField(db_column='ShippingFeeOld', max_digits=8, decimal_places=2)  # Field name made lowercase.
    shippingfee = models.DecimalField(db_column='ShippingFee', max_digits=8, decimal_places=2)  # Field name made lowercase.
    lastoperatetime = models.DateTimeField(db_column='LastOperateTime')  # Field name made lowercase.
    lastoperator = models.CharField(db_column='LastOperator', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotionorderspaychange'


class Promotionpackage(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotionpackage'


class Promotionpackageitem(models.Model):
    packageid = models.IntegerField(db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    targetid = models.CharField(db_column='targetId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotionpackageitem'


class Promotionpayback(models.Model):
    paybackcategory = models.IntegerField(db_column='paybackCategory', blank=True, null=True)  # Field name made lowercase.
    calculationtype = models.IntegerField(db_column='calculationType', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotionpayback'


class Promotiontopic(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)
    promotiontype = models.IntegerField(db_column='promotionType', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotiontopic'


class Promotionvoucher(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    vouchertemplateid = models.IntegerField(db_column='voucherTemplateId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotionvoucher'


class RActPav(models.Model):
    act = models.ForeignKey(OActivity, models.DO_NOTHING, db_column='ACT_ID', primary_key=True)  # Field name made lowercase.
    pav = models.ForeignKey(OPavilion, models.DO_NOTHING, db_column='PAV_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'r_act_pav'
        unique_together = (('act', 'pav'),)


class RActivityParticipant(models.Model):
    act = models.ForeignKey(OActivity, models.DO_NOTHING, db_column='ACT_ID')  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    attent_time = models.CharField(db_column='ATTENT_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mem_id = models.CharField(db_column='MEM_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    insert_timestamp = models.DateTimeField(db_column='INSERT_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='UPDATE_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.IntegerField(db_column='UPDATED_BY', blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey(DActPartSts, models.DO_NOTHING, db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    ractivityparticipantid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'r_activity_participant'


class RDishMaterial(models.Model):
    rdishMaterialid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dish_code = models.ForeignKey(ODish, models.DO_NOTHING, db_column='DISH_CODE')  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goodsn = models.CharField(db_column='GOODSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MATERIAL_NAME', max_length=200)  # Field name made lowercase.
    dosage = models.CharField(db_column='DOSAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_online_goods = models.CharField(db_column='IS_ONLINE_GOODS', max_length=1)  # Field name made lowercase.
    material_type = models.ForeignKey(DMaterialType, models.DO_NOTHING, db_column='MATERIAL_TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'r_dish_material'


class RDishNutrition(models.Model):
    dish_code = models.ForeignKey(ODish, models.DO_NOTHING, db_column='DISH_CODE')  # Field name made lowercase.
    nutrition_item = models.CharField(db_column='NUTRITION_ITEM', max_length=30)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    content = models.FloatField(db_column='CONTENT')  # Field name made lowercase.
    zhujianid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'r_dish_nutrition'


class RGroupbuyMember(models.Model):
    groupbuy_id = models.CharField(db_column='GROUPBUY_ID', primary_key=True, max_length=64)  # Field name made lowercase.
    member_id = models.CharField(db_column='MEMBER_ID', max_length=64)  # Field name made lowercase.
    member_role = models.IntegerField(db_column='MEMBER_ROLE', blank=True, null=True)  # Field name made lowercase.
    join_time = models.DateTimeField(db_column='JOIN_TIME', blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='ORDERID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pay_flag = models.IntegerField(db_column='PAY_FLAG', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'r_groupbuy_member'
        unique_together = (('groupbuy_id', 'member_id'),)


class RHotsaleGoods(models.Model):
    hotsaleid = models.CharField(db_column='hotSaleId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goods_sn = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_hotsale_goods'


class RShowGoods(models.Model):
    categoryid = models.PositiveIntegerField(db_column='categoryId')  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sn = models.CharField(max_length=32, blank=True, null=True)
    goodsalias = models.CharField(db_column='goodsAlias', max_length=128, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_show_goods'


class RWxGroupEggs(models.Model):
    egg_act = models.ForeignKey(OPaintedEggAct, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(DWxGroup, models.DO_NOTHING, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    remainder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_wx_group_eggs'


class Receivegift(models.Model):
    receiveid = models.AutoField(db_column='receiveId', primary_key=True)  # Field name made lowercase.
    giftshareid = models.IntegerField(db_column='giftShareId', blank=True, null=True)  # Field name made lowercase.
    receiveuserid = models.CharField(db_column='receiveUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(max_length=100, blank=True, null=True)
    headimg = models.TextField(blank=True, null=True)
    receivetime = models.DateTimeField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    giftdetailname = models.CharField(db_column='giftDetailName', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receivegift'


class RechargeDiscount(models.Model):
    rechargemoney = models.DecimalField(db_column='rechargeMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reward = models.CharField(max_length=4000, blank=True, null=True)
    discountmoney = models.DecimalField(db_column='discountMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    rewardmoney = models.DecimalField(db_column='rewardMoney', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recharge_discount'


class RedpackeBak(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=66, blank=True, null=True)  # Field name made lowercase.
    account = models.BigIntegerField(blank=True, null=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    中奖时间 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redpacke_bak'


class RedpackeBakk(models.Model):
    memberid = models.CharField(db_column='memberId', max_length=66, blank=True, null=True)  # Field name made lowercase.
    account = models.BigIntegerField(blank=True, null=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redpacke_bakk'


class Redpacket(models.Model):
    title = models.CharField(max_length=255)
    num = models.PositiveIntegerField(blank=True, null=True)
    enable = models.PositiveIntegerField(blank=True, null=True)
    starttime = models.PositiveIntegerField(blank=True, null=True)
    endtime = models.PositiveIntegerField(blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createby = models.IntegerField(blank=True, null=True)
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateby = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    shareicon = models.CharField(db_column='shareIcon', max_length=512)  # Field name made lowercase.
    sharetitle = models.CharField(db_column='shareTitle', max_length=128)  # Field name made lowercase.
    sharecontent = models.CharField(db_column='shareContent', max_length=512)  # Field name made lowercase.
    sharemessage = models.CharField(db_column='shareMessage', max_length=140)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'redpacket'


class Redpacketdetail(models.Model):
    rpid = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    templateid = models.IntegerField()
    probability = models.DecimalField(max_digits=12, decimal_places=10)
    thumbnailurl = models.CharField(max_length=500)
    detailurl = models.CharField(max_length=500)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createby = models.IntegerField(blank=True, null=True)
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateby = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    usedcount = models.IntegerField(db_column='usedCount', blank=True, null=True)  # Field name made lowercase.
    defaultselect = models.IntegerField(db_column='defaultSelect', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'redpacketdetail'


class Redpacketpageset(models.Model):
    rpid = models.IntegerField()
    topimg = models.CharField(db_column='topImg', max_length=512)  # Field name made lowercase.
    baseimg = models.CharField(db_column='baseImg', max_length=512)  # Field name made lowercase.
    activityimg = models.TextField(db_column='activityImg')  # Field name made lowercase.
    getstatusimg = models.CharField(db_column='getStatusImg', max_length=512)  # Field name made lowercase.
    sharestatusimg = models.CharField(db_column='shareStatusImg', max_length=512)  # Field name made lowercase.
    closestatusimg = models.CharField(db_column='closeStatusImg', max_length=512)  # Field name made lowercase.
    processingstatusimg = models.CharField(db_column='processingStatusImg', max_length=512)  # Field name made lowercase.
    winallstatusimg = models.CharField(db_column='winAllStatusImg', max_length=512)  # Field name made lowercase.
    redpacketwithoutstatusimg = models.CharField(db_column='redpacketWithoutStatusImg', max_length=512)  # Field name made lowercase.
    redpacketwithoutsecondstatusimg = models.CharField(db_column='redpacketWithoutSecondStatusImg', max_length=512)  # Field name made lowercase.
    redpacketwithoutfirststatusimg = models.CharField(db_column='redpacketWithoutFirstStatusImg', max_length=512)  # Field name made lowercase.
    redpacketgetallstatusimg = models.CharField(db_column='redpacketGetAllStatusImg', max_length=512)  # Field name made lowercase.
    bottomimg = models.TextField(db_column='bottomImg')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'redpacketpageset'


class Redpacketsrecord(models.Model):
    redpacketsid = models.IntegerField(db_column='redPacketsId', blank=True, null=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sharememberid = models.CharField(db_column='shareMemberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    frommemberid = models.CharField(db_column='fromMemberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'redpacketsrecord'


class Region(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=64, blank=True, null=True)
    pathname = models.CharField(db_column='pathName', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Replenishmentorderdetail(models.Model):
    replenishmentorderid = models.PositiveIntegerField(db_column='replenishmentOrderId', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    goodssn = models.CharField(db_column='goodsSn', max_length=30, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    goodstitle = models.CharField(db_column='goodsTitle', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cnt = models.PositiveSmallIntegerField(blank=True, null=True)
    marketprice = models.DecimalField(db_column='marketPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    realprice = models.DecimalField(db_column='realPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'replenishmentorderdetail'


class Replenishmentorders(models.Model):
    replenishmentorderid = models.AutoField(db_column='replenishmentOrderId', primary_key=True)  # Field name made lowercase.
    relatedorderid = models.PositiveIntegerField(db_column='relatedOrderId', blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ordertype = models.PositiveIntegerField(db_column='orderType', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.PositiveIntegerField(db_column='orderStatus', blank=True, null=True)  # Field name made lowercase.
    shippingstatus = models.PositiveIntegerField(db_column='shippingStatus', blank=True, null=True)  # Field name made lowercase.
    paystatus = models.PositiveIntegerField(db_column='payStatus', blank=True, null=True)  # Field name made lowercase.
    exceptionstatus = models.PositiveIntegerField(db_column='exceptionStatus', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.PositiveIntegerField(db_column='deliveryStatus', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    deliverytimebegin = models.PositiveIntegerField(db_column='deliveryTimeBegin', blank=True, null=True)  # Field name made lowercase.
    deliverytimeend = models.PositiveIntegerField(db_column='deliveryTimeEnd', blank=True, null=True)  # Field name made lowercase.
    shippingid = models.PositiveIntegerField(db_column='shippingId', blank=True, null=True)  # Field name made lowercase.
    shippingname = models.CharField(db_column='shippingName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    consignee = models.CharField(max_length=64, blank=True, null=True)
    payid = models.IntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    needtopay = models.DecimalField(db_column='needToPay', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    moneypaid = models.DecimalField(db_column='moneyPaid', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True)
    createtime = models.PositiveIntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    confirmtime = models.PositiveIntegerField(db_column='confirmTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.PositiveIntegerField(db_column='shippingTime', blank=True, null=True)  # Field name made lowercase.
    receivetime = models.PositiveIntegerField(db_column='receiveTime', blank=True, null=True)  # Field name made lowercase.
    closetime = models.PositiveIntegerField(db_column='closeTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.PositiveIntegerField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'replenishmentorders'


class Restoregoodsimg(models.Model):
    guid = models.CharField(max_length=64)
    imgpath = models.CharField(db_column='imgPath', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restoregoodsimg'


class Restoregoodsinfo(models.Model):
    guid = models.CharField(max_length=64)
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    recid = models.PositiveIntegerField(db_column='recId', blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=20)  # Field name made lowercase.
    restorenumber = models.IntegerField(db_column='restoreNumber')  # Field name made lowercase.
    description = models.CharField(max_length=200)
    restorestatus = models.IntegerField(db_column='restoreStatus')  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    restoreintegral = models.IntegerField(db_column='restoreIntegral', blank=True, null=True)  # Field name made lowercase.
    restorecontent = models.CharField(db_column='restoreContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    audittime = models.IntegerField(db_column='auditTime', blank=True, null=True)  # Field name made lowercase.
    ccbamount = models.DecimalField(db_column='ccbAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cmbamount = models.DecimalField(db_column='cmbAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    weixinamount = models.DecimalField(db_column='weixinAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alipayamount = models.DecimalField(db_column='alipayAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restoregoodsinfo'


class Restoreordersinfo(models.Model):
    orderid = models.IntegerField(db_column='orderId')  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=20)  # Field name made lowercase.
    guid = models.CharField(max_length=64)
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    audittime = models.IntegerField(db_column='auditTime', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='operatorId', blank=True, null=True)  # Field name made lowercase.
    restoreintegral = models.IntegerField(db_column='restoreIntegral', blank=True, null=True)  # Field name made lowercase.
    restorecontent = models.TextField(db_column='restoreContent', blank=True, null=True)  # Field name made lowercase.
    restorestatus = models.IntegerField(db_column='restoreStatus')  # Field name made lowercase.
    imgpath = models.TextField(db_column='imgPath', blank=True, null=True)  # Field name made lowercase.
    ccbamount = models.DecimalField(db_column='ccbAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cmbamount = models.DecimalField(db_column='cmbAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    weixinamount = models.DecimalField(db_column='weixinAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alipayamount = models.DecimalField(db_column='alipayAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restoreordersinfo'


class Restoresubmitinfo(models.Model):
    orderid = models.PositiveIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    restoreway = models.PositiveIntegerField(db_column='restoreWay', blank=True, null=True)  # Field name made lowercase.
    restoretype = models.PositiveIntegerField(db_column='restoreType', blank=True, null=True)  # Field name made lowercase.
    referenceid = models.IntegerField(db_column='referenceId', blank=True, null=True)  # Field name made lowercase.
    payid = models.PositiveIntegerField(db_column='payId', blank=True, null=True)  # Field name made lowercase.
    payname = models.CharField(db_column='payName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restoresubmitinfo'


class ShareInfo(models.Model):
    pid = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apppagepath = models.CharField(db_column='AppPagePath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    overtime = models.DateTimeField(db_column='Overtime', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=500, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'share_info'


class ShareInformation(models.Model):
    invitationcodetypeid = models.IntegerField(db_column='invitationcodetypeId', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    icon = models.CharField(max_length=500, blank=True, null=True)
    overtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'share_information'


class Shipping(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True, null=True)
    insure = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supportcod = models.PositiveIntegerField(db_column='supportCod', blank=True, null=True)  # Field name made lowercase.
    enabled = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping'


class Shippingareas(models.Model):
    areacode = models.CharField(db_column='areaCode', max_length=50)  # Field name made lowercase.
    areafullname = models.CharField(db_column='areaFullName', max_length=50)  # Field name made lowercase.
    areashortname = models.CharField(db_column='areaShortName', max_length=50)  # Field name made lowercase.
    parentid = models.PositiveIntegerField(db_column='parentId')  # Field name made lowercase.
    level = models.PositiveIntegerField()
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.
    isshipping = models.PositiveIntegerField(db_column='isShipping')  # Field name made lowercase.
    isenabled = models.PositiveIntegerField(db_column='isEnabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shippingareas'


class Shippingpoint(models.Model):
    shippingsiteid = models.IntegerField(db_column='shippingSiteId')  # Field name made lowercase.
    name = models.CharField(max_length=30)
    contactname = models.CharField(db_column='contactName', max_length=30)  # Field name made lowercase.
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    imgurl = models.CharField(db_column='imgUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    line = models.CharField(max_length=255)
    starthour = models.IntegerField(db_column='startHour', blank=True, null=True)  # Field name made lowercase.
    startminute = models.IntegerField(db_column='startMinute', blank=True, null=True)  # Field name made lowercase.
    endhour = models.IntegerField(db_column='endHour', blank=True, null=True)  # Field name made lowercase.
    endminute = models.IntegerField(db_column='endMinute', blank=True, null=True)  # Field name made lowercase.
    openinghours = models.CharField(db_column='openingHours', max_length=30, blank=True, null=True)  # Field name made lowercase.
    enabled = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shippingpoint'


class Shippingregion(models.Model):
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    parentcode = models.CharField(db_column='parentCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    depth = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shippingregion'


class Shippingsite(models.Model):
    name = models.CharField(max_length=150)
    shippingid = models.PositiveIntegerField(db_column='shippingId')  # Field name made lowercase.
    config = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'shippingsite'


class ShopRegion(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    regionid = models.IntegerField(db_column='regionId', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=256, blank=True, null=True)
    cityid = models.IntegerField(db_column='cityId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop_region'


class SsoApp(models.Model):
    appid = models.CharField(db_column='appId', max_length=45, blank=True, null=True)  # Field name made lowercase.
    appkey = models.CharField(db_column='appKey', max_length=16, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sso_app'


class Stockflushrecord(models.Model):
    recordid = models.AutoField(primary_key=True)
    goodssn = models.CharField(max_length=60, blank=True, null=True)
    goodsname = models.CharField(max_length=60, blank=True, null=True)
    goodsstock3 = models.IntegerField(blank=True, null=True)
    goodsnumber3 = models.IntegerField(blank=True, null=True)
    goodsstock4 = models.IntegerField(blank=True, null=True)
    goodsnumber4 = models.IntegerField(blank=True, null=True)
    flushdate = models.DateTimeField(blank=True, null=True)
    recordtype = models.IntegerField(db_column='recordType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stockflushrecord'


class Stockrealchange(models.Model):
    changeid = models.BigAutoField(db_column='changeId', primary_key=True)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    stockqty = models.IntegerField(db_column='stockQty', blank=True, null=True)  # Field name made lowercase.
    stockoldqty = models.IntegerField(db_column='stockOldQty', blank=True, null=True)  # Field name made lowercase.
    stocktype = models.IntegerField(db_column='stockType', blank=True, null=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='changeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stockrealchange'


class StockrealchangeHistory(models.Model):
    changeid = models.BigIntegerField(db_column='changeId', primary_key=True)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    stockqty = models.IntegerField(db_column='stockQty', blank=True, null=True)  # Field name made lowercase.
    stockoldqty = models.IntegerField(db_column='stockOldQty', blank=True, null=True)  # Field name made lowercase.
    stocktype = models.IntegerField(db_column='stockType', blank=True, null=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='changeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stockrealchange_history'


class StockrealchangeTmp(models.Model):
    changeid = models.BigIntegerField(db_column='changeId')  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    stockqty = models.IntegerField(db_column='stockQty', blank=True, null=True)  # Field name made lowercase.
    stockoldqty = models.IntegerField(db_column='stockOldQty', blank=True, null=True)  # Field name made lowercase.
    stocktype = models.IntegerField(db_column='stockType', blank=True, null=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='changeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stockrealchange_tmp'


class Sysapistatistic(models.Model):
    operator = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=50, blank=True, null=True)
    data = models.CharField(max_length=512, blank=True, null=True)
    client = models.CharField(max_length=30, blank=True, null=True)
    device = models.CharField(max_length=50, blank=True, null=True)
    geolocation = models.CharField(db_column='geoLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=30, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysapistatistic'


class Sysdepartment(models.Model):
    name = models.CharField(max_length=128)
    path = models.CharField(max_length=512)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)
    displayorder = models.IntegerField(db_column='displayOrder', blank=True, null=True)  # Field name made lowercase.
    isdir = models.TextField(db_column='isDir', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sysdepartment'


class SysdeptPos(models.Model):
    departmentid = models.IntegerField(db_column='departmentId', primary_key=True)  # Field name made lowercase.
    positionid = models.IntegerField(db_column='positionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysdept_pos'
        unique_together = (('departmentid', 'positionid'),)


class SysdeptUserPer(models.Model):
    departmentid = models.IntegerField(db_column='departmentId', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    permissionid = models.IntegerField(db_column='permissionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysdept_user_per'
        unique_together = (('departmentid', 'userid', 'permissionid'),)


class SysdeptUserPos(models.Model):
    departmentid = models.IntegerField(db_column='departmentId', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    positionid = models.IntegerField(db_column='positionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysdept_user_pos'
        unique_together = (('departmentid', 'userid', 'positionid'),)


class SysdeptUserRole(models.Model):
    departmentid = models.IntegerField(db_column='departmentId', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysdept_user_role'
        unique_together = (('departmentid', 'userid', 'roleid'),)


class Syslog(models.Model):
    operator = models.IntegerField(blank=True, null=True)
    table = models.CharField(max_length=50, blank=True, null=True)
    operation = models.CharField(max_length=50, blank=True, null=True)
    data = models.CharField(max_length=5000, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    detail = models.CharField(max_length=5000, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syslog'


class SyslogCopy(models.Model):
    operator = models.IntegerField(blank=True, null=True)
    table = models.CharField(max_length=50, blank=True, null=True)
    operation = models.CharField(max_length=50, blank=True, null=True)
    data = models.CharField(max_length=5000, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    detail = models.CharField(max_length=5000, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syslog_copy'


class SysperRole(models.Model):
    permissionid = models.IntegerField(db_column='permissionId', primary_key=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysper_role'
        unique_together = (('permissionid', 'roleid'),)


class Syspermission(models.Model):
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=256)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(max_length=512, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)
    isactive = models.TextField(db_column='isActive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cssclass = models.CharField(db_column='cssClass', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdir = models.TextField(db_column='isDir', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ismenu = models.TextField(db_column='isMenu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isrestful = models.TextField(db_column='isRestful', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    restfultype = models.IntegerField(db_column='restfulType', blank=True, null=True)  # Field name made lowercase.
    restfultarget = models.CharField(db_column='restfulTarget', max_length=32, blank=True, null=True)  # Field name made lowercase.
    restfulflag = models.CharField(db_column='restfulFlag', max_length=64, blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='displayOrder', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)
    conditionsql = models.CharField(db_column='conditionSQL', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syspermission'


class SysposRole(models.Model):
    positionid = models.IntegerField(db_column='positionId', primary_key=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syspos_role'
        unique_together = (('positionid', 'roleid'),)


class Sysposition(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysposition'


class Sysrole(models.Model):
    name = models.CharField(max_length=256)
    isactive = models.TextField(db_column='isActive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    displayorder = models.IntegerField(db_column='displayOrder', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysrole'


class Syssetting(models.Model):
    name = models.CharField(max_length=65)
    key = models.CharField(max_length=65)
    value = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syssetting'


class Sysuser(models.Model):
    sn = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(db_column='userName', max_length=128)  # Field name made lowercase.
    displayname = models.CharField(db_column='displayName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='passwordHash', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isactive = models.TextField(db_column='isActive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    salt = models.IntegerField(blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysuser'


class TActPic(models.Model):
    act_id = models.CharField(max_length=64)
    path = models.CharField(max_length=255, blank=True, null=True)
    pic_type = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_act_pic'


class TGroupCart(models.Model):
    goodsn = models.CharField(db_column='goodSN', max_length=32)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=64)  # Field name made lowercase.
    cnt = models.IntegerField()
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    payendtime = models.DateTimeField(db_column='payEndTime')  # Field name made lowercase.
    inserttime = models.DateTimeField(db_column='insertTime')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    goodguid = models.CharField(db_column='goodGuid', max_length=64)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='isCheck', blank=True, null=True)  # Field name made lowercase.
    goodamount = models.DecimalField(db_column='goodAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='discountAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountedamount = models.DecimalField(db_column='discountedAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_group_cart'




class TGroupCartHis(models.Model):
    pid = models.IntegerField(primary_key=True)
    goodsn = models.CharField(db_column='goodSN', max_length=32)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=64)  # Field name made lowercase.
    cnt = models.IntegerField()
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    payendtime = models.DateTimeField(db_column='payEndTime')  # Field name made lowercase.
    inserttime = models.DateTimeField(db_column='insertTime')  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    goodguid = models.CharField(db_column='goodGuid', max_length=64)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='isCheck', blank=True, null=True)  # Field name made lowercase.
    goodamount = models.DecimalField(db_column='goodAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='discountAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountedamount = models.DecimalField(db_column='discountedAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_group_cart_his'


class TGroupbuy(models.Model):
    groupbuy_id = models.CharField(db_column='GROUPBUY_ID', primary_key=True, max_length=64)  # Field name made lowercase.
    hotsale_id = models.CharField(db_column='HOTSALE_ID', max_length=64)  # Field name made lowercase.
    member_id = models.CharField(db_column='MEMBER_ID', max_length=64)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    found_time = models.DateTimeField(db_column='FOUND_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    pay_end_time = models.DateTimeField(db_column='PAY_END_TIME', blank=True, null=True)  # Field name made lowercase.
    member_number = models.IntegerField(db_column='MEMBER_NUMBER', blank=True, null=True)  # Field name made lowercase.
    groupbuy_flag = models.IntegerField(db_column='GROUPBUY_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_groupbuy'


class THotsaleExtend(models.Model):
    pid = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    hotsale_id = models.CharField(db_column='HotSale_ID', max_length=64)  # Field name made lowercase.
    producing_area = models.CharField(db_column='PRODUCING_AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hotsale_extend'


class THotsaleImage(models.Model):
    image_id = models.CharField(db_column='IMAGE_ID', primary_key=True, max_length=64)  # Field name made lowercase.
    hotsale_id = models.CharField(db_column='HOTSALE_ID', max_length=64)  # Field name made lowercase.
    image_type = models.IntegerField(db_column='IMAGE_TYPE', blank=True, null=True)  # Field name made lowercase.
    image_description = models.CharField(db_column='IMAGE_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_num = models.IntegerField(db_column='SORT_NUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_hotsale_image'


class TPavPic(models.Model):
    pav = models.ForeignKey(OPavilion, models.DO_NOTHING)
    pic_type = models.ForeignKey(DPicType, models.DO_NOTHING, db_column='pic_type', blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pav_pic'


class TShow(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    cook_time = models.IntegerField(db_column='COOK_TIME', blank=True, null=True)  # Field name made lowercase.
    diffculty_idx = models.IntegerField(db_column='DIFFCULTY_IDX', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    create_timestamp = models.DateTimeField(db_column='CREATE_TIMESTAMP')  # Field name made lowercase.
    publish_time = models.DateTimeField(db_column='PUBLISH_TIME', blank=True, null=True)  # Field name made lowercase.
    member_id = models.CharField(db_column='MEMBER_ID', max_length=64)  # Field name made lowercase.
    vote_cnt = models.DecimalField(db_column='VOTE_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    product_pic = models.CharField(db_column='PRODUCT_PIC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dish_id = models.CharField(db_column='DISH_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    template_id = models.CharField(db_column='TEMPLATE_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_show'


class TShowComment(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    show_id = models.IntegerField(db_column='SHOW_ID')  # Field name made lowercase.
    member_id = models.CharField(db_column='MEMBER_ID', max_length=100)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID')  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=1000)  # Field name made lowercase.
    comment_date = models.DateTimeField(db_column='COMMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    delete_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_show_comment'


class TShowExperts(models.Model):
    picture = models.CharField(max_length=255)
    pic_name = models.CharField(max_length=255)
    experts_url = models.CharField(max_length=255, blank=True, null=True)
    is_top = models.IntegerField()
    top_time = models.DateTimeField(blank=True, null=True)
    is_display = models.IntegerField()
    member_id = models.CharField(max_length=255)
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_show_experts'


class TShowHeadFigure(models.Model):
    related_id = models.IntegerField()
    title = models.CharField(max_length=11)
    pic_link = models.CharField(max_length=255)
    content_link = models.CharField(max_length=255)
    type = models.IntegerField()
    is_top = models.IntegerField(blank=True, null=True)
    top_time = models.DateTimeField(blank=True, null=True)
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_show_head_figure'


class TShowKeywordHot(models.Model):
    keyword = models.CharField(unique=True, max_length=255)
    quantity = models.IntegerField()
    is_top = models.IntegerField(blank=True, null=True)
    delete_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_show_keyword_hot'
        unique_together = (('id', 'keyword', 'quantity'),)


class TShowMaterial(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    show_id = models.IntegerField(db_column='SHOW_ID', blank=True, null=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MATERIAL_NAME', max_length=30)  # Field name made lowercase.
    dosage = models.CharField(db_column='DOSAGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    material_type = models.IntegerField(db_column='MATERIAL_TYPE', blank=True, null=True)  # Field name made lowercase.
    src = models.IntegerField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='DISH_ID', blank=True, null=True)  # Field name made lowercase.
    parts_id = models.CharField(db_column='PARTS_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_show_material'


class TShowReportList(models.Model):
    pid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.CharField(db_column='MEMBER_ID', max_length=50)  # Field name made lowercase.
    show_id = models.IntegerField(db_column='SHOW_ID')  # Field name made lowercase.
    report_date = models.DateTimeField(db_column='REPORT_DATE')  # Field name made lowercase.
    reason = models.CharField(db_column='REASON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_show_report_list'


class TShowSolutions(models.Model):
    show_id = models.IntegerField()
    category_id = models.IntegerField()
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_show_solutions'


class TShowSolutionsCategory(models.Model):
    title = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    pic_name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    position = models.IntegerField()
    is_display = models.IntegerField()
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_show_solutions_category'


class TShowStep(models.Model):
    step_id = models.AutoField(db_column='STEP_ID', primary_key=True)  # Field name made lowercase.
    show_id = models.IntegerField(db_column='SHOW_ID')  # Field name made lowercase.
    pic = models.CharField(db_column='PIC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_show_step'


class TShowTop(models.Model):
    show_id = models.IntegerField()
    is_top = models.IntegerField()
    top_time = models.DateTimeField()
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_show_top'


class TShowVoteList(models.Model):
    show_id = models.IntegerField(db_column='SHOW_ID')  # Field name made lowercase.
    mem_id = models.CharField(db_column='MEM_ID', max_length=50)  # Field name made lowercase.
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_show_vote_list'


class Tag(models.Model):
    typeid = models.IntegerField(db_column='typeId')  # Field name made lowercase.
    name = models.CharField(max_length=64)
    referencecount = models.IntegerField(db_column='referenceCount')  # Field name made lowercase.
    condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class Tagreference(models.Model):
    key = models.CharField(max_length=64)
    tagid = models.IntegerField(db_column='tagId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tagreference'


class Tagtype(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'tagtype'


class Temp3Goodsinfo(models.Model):
    goodssn = models.CharField(db_column='goodsSn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    goodsnumber = models.IntegerField(db_column='goodsNumber')  # Field name made lowercase.
    goodsstock = models.IntegerField(db_column='goodsStock')  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', primary_key=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp3goodsinfo'


class Templatearea(models.Model):
    aid = models.AutoField(db_column='aId', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='areaName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    areatype = models.IntegerField(db_column='areaType', blank=True, null=True)  # Field name made lowercase.
    atid = models.IntegerField(db_column='aTId', blank=True, null=True)  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=64, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=255)  # Field name made lowercase.
    templatetype = models.IntegerField(db_column='templateType', blank=True, null=True)  # Field name made lowercase.
    buttonposition = models.IntegerField(db_column='buttonPosition', blank=True, null=True)  # Field name made lowercase.
    displayseq = models.IntegerField(db_column='displaySeq', blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'templatearea'


class Templateareashelves(models.Model):
    aid = models.IntegerField(db_column='aId')  # Field name made lowercase.
    goodsguid = models.CharField(db_column='goodsGuid', max_length=50)  # Field name made lowercase.
    displayseq = models.IntegerField(db_column='displaySeq', blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'templateareashelves'


class Testlog(models.Model):
    message_body = models.CharField(max_length=500, blank=True, null=True)
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testlog'


class Thirdcertification(models.Model):
    thirdid = models.CharField(db_column='thirdId', primary_key=True, max_length=64)  # Field name made lowercase.
    thirdtype = models.IntegerField(db_column='thirdType', blank=True, null=True)  # Field name made lowercase.
    thirdname = models.CharField(db_column='thirdName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    openid = models.CharField(db_column='openId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accesstoken = models.CharField(db_column='accessToken', max_length=200, blank=True, null=True)  # Field name made lowercase.
    refreshtoken = models.CharField(db_column='refreshToken', max_length=200, blank=True, null=True)  # Field name made lowercase.
    scope = models.CharField(max_length=200, blank=True, null=True)
    unionid = models.CharField(db_column='unionId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='mobilePhone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=2000, blank=True, null=True)
    createdata = models.DateTimeField(db_column='createData', blank=True, null=True)  # Field name made lowercase.
    updatedata = models.DateTimeField(db_column='updateData', blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thirdcertification'


class Thirdcertificationdeletelog(models.Model):
    thirdid = models.CharField(db_column='thirdId', max_length=64)  # Field name made lowercase.
    thirdtype = models.IntegerField(db_column='thirdType', blank=True, null=True)  # Field name made lowercase.
    thirdname = models.CharField(db_column='thirdName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    openid = models.CharField(db_column='openId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accesstoken = models.CharField(db_column='accessToken', max_length=200, blank=True, null=True)  # Field name made lowercase.
    refreshtoken = models.CharField(db_column='refreshToken', max_length=200, blank=True, null=True)  # Field name made lowercase.
    scope = models.CharField(max_length=200, blank=True, null=True)
    unionid = models.CharField(db_column='unionId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='mobilePhone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=2000, blank=True, null=True)
    createdata = models.DateTimeField(db_column='createData', blank=True, null=True)  # Field name made lowercase.
    updatedata = models.DateTimeField(db_column='updateData', blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.
    deletedata = models.DateTimeField(db_column='deleteData', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='operatorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thirdcertificationdeletelog'


class Tmpdeliverystatus(models.Model):
    ordersn = models.CharField(db_column='orderSn', max_length=60, blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.IntegerField(db_column='deliveryStatus', blank=True, null=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='changeDate', blank=True, null=True)  # Field name made lowercase.
    paystatus = models.IntegerField(db_column='payStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpdeliverystatus'


class UnMembershippingtime(models.Model):
    deviceid = models.CharField(db_column='deviceId', primary_key=True, max_length=100)  # Field name made lowercase.
    shippingdate = models.IntegerField(db_column='shippingDate', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    shippingtime = models.CharField(db_column='shippingTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addressid = models.IntegerField(db_column='addressId')  # Field name made lowercase.
    isdfault = models.IntegerField(db_column='isDfault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'un_membershippingtime'


class Uniqueloginip(models.Model):
    androidold = models.CharField(max_length=10, blank=True, null=True)
    androidnew = models.CharField(max_length=10, blank=True, null=True)
    iosold = models.CharField(max_length=10, blank=True, null=True)
    iosnew = models.CharField(max_length=10, blank=True, null=True)
    h5new = models.CharField(max_length=10, blank=True, null=True)
    calcate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uniqueloginip'


class Vendorinvoice(models.Model):
    vendorid = models.CharField(db_column='vendorId', primary_key=True, max_length=64)  # Field name made lowercase.
    title = models.CharField(max_length=64, blank=True, null=True)
    companyname = models.CharField(db_column='companyName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    identificationnum = models.CharField(db_column='identificationNum', max_length=64, blank=True, null=True)  # Field name made lowercase.
    drawer = models.CharField(max_length=64, blank=True, null=True)
    receiver = models.CharField(max_length=64, blank=True, null=True)
    reviewer = models.CharField(max_length=64, blank=True, null=True)
    createdtime = models.IntegerField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendorinvoice'


class Verificationcodehistorylog(models.Model):
    vcode_id = models.PositiveIntegerField(primary_key=True)
    phone = models.CharField(max_length=100)
    vcode = models.CharField(max_length=50)
    add_time = models.IntegerField()
    errorcount = models.IntegerField(db_column='errorCount')  # Field name made lowercase.
    type = models.CharField(max_length=1)
    apiname = models.CharField(db_column='apiName', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'verificationcodehistorylog'


class Verificationcodelog(models.Model):
    vcode_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=100)
    vcode = models.CharField(max_length=50)
    add_time = models.IntegerField()
    errorcount = models.IntegerField(db_column='errorCount', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=1)
    apiname = models.CharField(db_column='apiName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'verificationcodelog'


class VerificationcodelogHistory(models.Model):
    vcode_id = models.PositiveIntegerField(primary_key=True)
    phone = models.CharField(max_length=100)
    vcode = models.CharField(max_length=50)
    add_time = models.IntegerField()
    errorcount = models.IntegerField(db_column='errorCount', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=1)
    apiname = models.CharField(db_column='apiName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'verificationcodelog_history'


class Voucherarea(models.Model):
    voucherareaid = models.AutoField(db_column='voucherAreaId', primary_key=True)  # Field name made lowercase.
    aid = models.IntegerField(db_column='aId')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    frequencytype = models.IntegerField(db_column='frequencyType')  # Field name made lowercase.
    frequencyvalue = models.IntegerField(db_column='frequencyValue')  # Field name made lowercase.
    templateids = models.CharField(db_column='templateIds', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    displayindex = models.IntegerField(db_column='displayIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voucherarea'


class Voucherarealog(models.Model):
    logid = models.AutoField(db_column='logId', primary_key=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='memberId', max_length=64)  # Field name made lowercase.
    atid = models.IntegerField(db_column='aTId')  # Field name made lowercase.
    aid = models.IntegerField(db_column='aId')  # Field name made lowercase.
    voucherid = models.BigIntegerField(db_column='voucherId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voucherarealog'


class Voucherpool(models.Model):
    pid = models.BigAutoField(db_column='id',primary_key=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    sn = models.CharField(max_length=255, blank=True, null=True)
    generatedtime = models.IntegerField(db_column='generatedTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    activedtime = models.IntegerField(db_column='activedTime', blank=True, null=True)  # Field name made lowercase.
    usedby = models.CharField(db_column='usedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    usedtime = models.IntegerField(db_column='usedTime', blank=True, null=True)  # Field name made lowercase.
    invalidated = models.IntegerField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    isassigned = models.TextField(db_column='isAssigned', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    user_id_old = models.IntegerField(blank=True, null=True)
    order_id_old = models.IntegerField(blank=True, null=True)
    coupon_id_old = models.IntegerField(blank=True, null=True)
    wxnotice = models.IntegerField(db_column='WXNotice', blank=True, null=True)  # Field name made lowercase.
    wxnoticetime = models.IntegerField(db_column='WXNoticeTime', blank=True, null=True)  # Field name made lowercase.
    messagenotice = models.IntegerField(db_column='messageNotice', blank=True, null=True)  # Field name made lowercase.
    messagenoticetime = models.IntegerField(db_column='messageNoticeTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voucherpool'


class VoucherpoolHistory(models.Model):
    pid = models.BigIntegerField(db_column='id',primary_key=True)
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    sn = models.CharField(max_length=255, blank=True, null=True)
    generatedtime = models.IntegerField(db_column='generatedTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    activedtime = models.IntegerField(db_column='activedTime', blank=True, null=True)  # Field name made lowercase.
    usedby = models.CharField(db_column='usedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    usedtime = models.IntegerField(db_column='usedTime', blank=True, null=True)  # Field name made lowercase.
    invalidated = models.IntegerField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    isassigned = models.TextField(db_column='isAssigned', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    user_id_old = models.IntegerField(blank=True, null=True)
    order_id_old = models.IntegerField(blank=True, null=True)
    coupon_id_old = models.IntegerField(blank=True, null=True)
    wxnotice = models.IntegerField(db_column='WXNotice', blank=True, null=True)  # Field name made lowercase.
    wxnoticetime = models.IntegerField(db_column='WXNoticeTime', blank=True, null=True)  # Field name made lowercase.
    messagenotice = models.IntegerField(db_column='messageNotice', blank=True, null=True)  # Field name made lowercase.
    messagenoticetime = models.IntegerField(db_column='messageNoticeTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voucherpool_history'


class VoucherpoolUpdate(models.Model):
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    sn = models.CharField(max_length=255, blank=True, null=True)
    generatedtime = models.IntegerField(db_column='generatedTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    activedtime = models.IntegerField(db_column='activedTime', blank=True, null=True)  # Field name made lowercase.
    usedby = models.CharField(db_column='usedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    usedtime = models.IntegerField(db_column='usedTime', blank=True, null=True)  # Field name made lowercase.
    invalidated = models.IntegerField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=255, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    isassigned = models.TextField(db_column='isAssigned', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coupon_id_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucherpool_update'


class Vouchertemplate(models.Model):
    name = models.CharField(max_length=55, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=64, blank=True, null=True)
    expirationtype = models.IntegerField(db_column='expirationType', blank=True, null=True)  # Field name made lowercase.
    validdates = models.IntegerField(db_column='validDates', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    imageurls = models.CharField(db_column='imageUrls', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invalidated = models.TextField(blank=True, null=True)  # This field type is a guess.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    ispublic = models.TextField(db_column='isPublic')  # Field name made lowercase. This field type is a guess.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    subtype = models.IntegerField(db_column='subType', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vouchertemplate'


class Voucherusecondition(models.Model):
    vouchertemplateid = models.IntegerField(db_column='voucherTemplateId', blank=True, null=True)  # Field name made lowercase.
    minamount = models.DecimalField(db_column='minAmount', max_digits=11, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    firstorder = models.TextField(db_column='firstOrder', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paytype = models.IntegerField(db_column='payType', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    goodtagids = models.CharField(db_column='goodTagIds', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deliverytimes = models.CharField(db_column='deliveryTimes', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voucherusecondition'


class WPageinfo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    keywords = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_pageinfo'


class WaInvite(models.Model):
    inviteid = models.AutoField(db_column='InviteId', primary_key=True)  # Field name made lowercase.
    invitecode = models.CharField(db_column='InviteCode', max_length=255)  # Field name made lowercase.
    usagecount = models.IntegerField(db_column='UsageCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wa_invite'


class Watermarktagrel(models.Model):
    watermarktagrelid = models.AutoField(db_column='watermarkTagRelId', primary_key=True)  # Field name made lowercase.
    watermarkid = models.IntegerField(db_column='watermarkId', blank=True, null=True)  # Field name made lowercase.
    tagid = models.IntegerField(db_column='tagId', blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='createUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.CharField(db_column='updateUserId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.IntegerField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'watermarktagrel'


class Weixinsubscribelog(models.Model):
    openid = models.CharField(db_column='openId', max_length=256)  # Field name made lowercase.
    channelplan = models.CharField(db_column='channelPlan', max_length=256)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='creationTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weixinsubscribelog'


class WicplatformMemberfromreach(models.Model):
    cardnumber = models.CharField(db_column='cardNumber', max_length=255)  # Field name made lowercase.
    telephone = models.CharField(max_length=50)
    usertype = models.IntegerField(db_column='userType')  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wicplatform.memberfromreach'


class WxAccesstoken(models.Model):
    accesstoken = models.CharField(db_column='accessToken', max_length=600, blank=True, null=True)  # Field name made lowercase.
    expiresin = models.DateTimeField(db_column='expiresIn', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wx_accesstoken'


class WxJsapiticket(models.Model):
    appid = models.CharField(max_length=60)
    jsapiticket = models.CharField(max_length=600, blank=True, null=True)
    expiresin = models.DateTimeField(db_column='expiresIn', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wx_jsapiticket'


class WxyCoupon(models.Model):
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    couponcode = models.CharField(db_column='couponCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    isused = models.IntegerField(db_column='isUsed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wxy_coupon'


class WxyCoupontemplate(models.Model):
    pid = models.IntegerField(db_column='id',primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    minamount = models.IntegerField(db_column='minAmount', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(blank=True, null=True)
    expirationtime = models.IntegerField(db_column='expirationTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wxy_coupontemplate'


class WxyProvidelog(models.Model):
    usedaccount = models.CharField(db_column='usedAccount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(max_length=200, blank=True, null=True)
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    ordersn = models.CharField(db_column='orderSn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    couponcode = models.CharField(db_column='couponCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wxy_providelog'


class AfterSalesType(models.Model):
    aftersalestypeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'after_sales_type'

class DutyDeptType(models.Model):
    deptsid = models.AutoField(db_column='deptsId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, default='0')

    class Meta:
        managed = False
        db_table = 'duty_dept_type'

class orderDetailList(models.Model):
    orderid = models.AutoField(db_column='orderid', primary_key=True)
    goodssn = models.CharField(db_column='goodssn', max_length=60)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsname', max_length=120)  # Field name made lowercase.
    goodsqty = models.IntegerField(db_column='goodsQTY', null=True)

    class Meta:
        managed = False
        db_table = 't2'

class GoodsRecommendShelfManager(models.Manager):
    def all(self):
        return super(GoodsRecommendShelfManager,self).all().filter(isdel=False)

class GoodsRecommendShelf(models.Model):
    guid = models.CharField(primary_key=True, max_length=64,db_column='guid',default=uuid.uuid1())
    goodsinfo = models.ForeignKey(Goodsinfo,on_delete=models.DO_NOTHING,related_name='goodsinfo',db_column='goodsguid')
    sn = models.CharField(max_length=32,blank=True, null=True)
    name = models.CharField(max_length=255,blank=True, null=True)
    goodslocation = models.IntegerField(db_column='goodsLocation',default=1)  # Field name made lowercase.
    goodssort = models.IntegerField(db_column='goodsSort',default=999)  # Field name made lowercase.
    createdata = models.DateTimeField(db_column='createData', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    updatedata = models.DateTimeField(db_column='updateData', blank=True, null=True,auto_now=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True,default=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsrecommendshelf'

    def __str__(self):
        return '%s %s %s %s' % (self.guid, self.name, self.goodslocation, self.goodssort)

    objects = GoodsRecommendShelfManager()