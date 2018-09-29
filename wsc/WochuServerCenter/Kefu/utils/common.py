import time

def complaintstypeFilter(x):
    return {
        -1: '-',
        0: '单品退款',
        1: '整单退款',
    }[x]

def aftersalestypeidFilter(list, aftersalestypeid):
    try:
        TEST = list.get(aftersalestypeid=aftersalestypeid)
        return TEST.name
    except:
        return '-'

def authuserFilter(list, userid):
    try:
        TEST = list.get(pid=userid)
        return TEST.username
    except:
        return '-'


def sourceFilter(x):
    try:
        return {
            -1: '-',
            0: '-',
            1: '顾客',
            2: '配送员',
            3: '物流',
            4: '自主退换货',
            5: 'APP意见反馈箱',
            6: '商品评论',
            7: '订单评论',
            8: '内部人员',
            9: '微博',
            10: '微信号',
            11: '彩蛋群',
            12: '其他'
        }[x]
    except:
        return '-'

def isreshipFilter(x):
    try:
        return {
            -1: '-',
            1: '补货',
            2: '不补货',
        }[x]
    except:
        return '-'

def isrefundFilter(x):
    try:
        return {
            -1: '-',
            1: '退款',
            2: '不退款',
        }[x]
    except:
        return '-'


def orderstatusFilter(x):
    try:
        return {
            -1: '-',
            0: '未确认',
            1: '已确认',
            2: '已取消',
            3: '无效',
            4: '退货',
            5: '已分单',
            6: '部分分单',
            7: '退货入库',
            8: '退款',
            9: '已评价',
            99: '已移除'
        }[x]
    except:
        return '-'


def refundchannelFilter(x):
    try:
        return {
            0: '微商城',
            1: '微信',
            2: '支付宝',
            3: '银联',
            4: 'apple'
        }[x]
    except:
        return '-'


def timeStampTOdatetime(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def transferGoodsMonitor(list):
    resultList = []
    for item in list:
        resultList.append({
            "goodsSn": item[0],
            "goodsName": item[1],
            "goodsQTY": item[2],
            "orderId": item[3],
            "id": item[4]
        })
    return resultList

def transferGoodsRealTimeInfo(list):
    resultList = []
    for item in list:
        resultList.append({
            "goodsSn": item[0],
            "goodsName": item[1],
            "goodsInfo": item[2]
        })
    return resultList