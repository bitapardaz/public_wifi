from django.db import models

# Create your modelModels: here.
class Owner(models.Model):
    phone_number = models.CharField(max_length=200,null=True,blank=True)
    owner_name = models.CharField(max_length=200,null=True,blank=True)
    owner_mobile = models.CharField(max_length=200,null=True,blank=True)
    #last_p2p_update = models.DateTimeField(null=True,blank=True)

class Device(models.Model):
    identification_code = models.CharField(max_length=200,null=True,blank=True)
    owner = models.ForeignKey(Owner)
    last_location = models.CharField(max_length=200,null=True,blank=True)
    last_ping = models.DateTimeField(null=True,blank=True)

    #data_allowance
    #sms_allowance
    #minutes_allowance

class VoucherType(models.Model):
    title = models.CharField(max_length=20)
    duration_days = models.IntegerField(default=1)

class Voucher(models.Model):
    device = models.ForeignKey(Device)
    is_sent_to_driver = models.BooleanField(default=False)
    is_consumed = models.BooleanField(default =False)
    date_generated = models.DateTimeField(auto_now=True)
    date_activated_by_consumer = models.DateTimeField()
    voucher_type = models.ForeignKey(VoucherType)

    # Customer who used the voucher, optional fields
    consumer_id = models.CharField(max_length=200,blank=True,null=True)
    consumer_mobile_phone = models.CharField(max_length=200,blank=True,null=True)


class Configuration(models.Model):
    corrent_voucher_code_entered = models.CharField(max_length=1000)
    wrong_voucher_code_entered = models.CharField(max_length=1000)
