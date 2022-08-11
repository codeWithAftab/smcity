from device.models import device, device_type_availaable, dustbin, washroom, waterpoint
from django.contrib import admin

# Register your models here.

admin.site.register(device)
admin.site.register(dustbin)
admin.site.register(waterpoint)
admin.site.register(washroom)
admin.site.register(device_type_availaable)