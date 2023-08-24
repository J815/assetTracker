from django.contrib import admin

from .models import Company,Employee,DeviceType,Device,DeviceLog
# Register your models here.
admin.site.register(Company)
admin.site.register(DeviceLog)
admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(Employee)