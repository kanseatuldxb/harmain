import django_filters
from .models import *

class GatewayTimeRangeFilter(django_filters.FilterSet):
    gateway_time__gte = django_filters.IsoDateTimeFilter(field_name='gateway_time', lookup_expr='gte')
    gateway_time__lte = django_filters.IsoDateTimeFilter(field_name='gateway_time', lookup_expr='lte')

    class Meta:
        model = EnergyMeterLog
        fields = ['device_name', 'dev_eui', 'gateway_time__gte', 'gateway_time__lte']

class GenericLogFilter(django_filters.FilterSet):
    gateway_time__gte = django_filters.IsoDateTimeFilter(field_name='gateway_time', lookup_expr='gte')
    gateway_time__lte = django_filters.IsoDateTimeFilter(field_name='gateway_time', lookup_expr='lte')

    class Meta:
        fields = ['device_name', 'gateway_time__gte', 'gateway_time__lte']
