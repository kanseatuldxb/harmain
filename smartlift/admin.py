from django.contrib import admin
from .models import LiftEnvironmentLog
from .models import LiftControlLog
from .models import LiftDoorEventLog
from .models import LiftOccupancyLog
from .models import EnergyMeterLog
from .models import LiftFloorEventLog

@admin.register(LiftFloorEventLog)
class LiftFloorArrivalLogAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'floor_number', 'qr_code', 'gateway_time')
    list_filter = ('device_name', 'floor_number', 'gateway_time')

@admin.register(EnergyMeterLog)
class EnergyMeterLogAdmin(admin.ModelAdmin):
    list_display = (
        'device_name', 'dev_eui', 'gateway_time',
        'kwh_value', 'e_scale', 'kwh_raw', 'received_at'
    )
    list_filter = ('device_name', 'gateway_time')
    search_fields = ('dev_eui', 'device_name')
    ordering = ('-gateway_time',)


@admin.register(LiftOccupancyLog)
class LiftOccupancyLogAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'people_count_all', 'region_count', 'gateway_time')
    list_filter = ('device_name', 'gateway_time')

@admin.register(LiftDoorEventLog)
class LiftDoorEventLogAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'event_type', 'gateway_time', 'text')
    list_filter = ('event_type', 'device_name')

@admin.register(LiftEnvironmentLog)
class LiftEnvironmentLogAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'temperature', 'humidity', 'gateway_time')
    list_filter = ('device_name', 'gateway_time')
    search_fields = ('device_name', 'topic')
    ordering = ('-gateway_time',)

@admin.register(LiftControlLog)
class LiftControlLogAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'gateway_time', 'gpio_input_1','gpio_input_2', 'gpio_counter_3', 'gpio_input_4')
    list_filter = ('device_name', 'gateway_time')