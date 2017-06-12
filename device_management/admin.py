from django.contrib import admin

# Register your models here.
from models import Owner, Device, VoucherType, Voucher,Configuration

admin.site.register(Owner)
admin.site.register(Device)
admin.site.register(VoucherType)
admin.site.register(Voucher)
admin.site.register(Configuration)
