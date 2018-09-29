from django.contrib import admin
from Kefu.models import AfterSalesType, AuthUser, Orderinvoicerecords, DutyDeptType, Orders, Offlinerefundorderslog, Offlinerefundorderslogdetail, Orderdetail

# Register your models here.
admin.site.register(AfterSalesType)
admin.site.register(AuthUser)
admin.site.register(Orderinvoicerecords)
admin.site.register(DutyDeptType)
admin.site.register(Orders)
admin.site.register(Offlinerefundorderslog)
admin.site.register(Offlinerefundorderslogdetail)
admin.site.register(Orderdetail)