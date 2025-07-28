from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

            

def index(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "lift_logs",
        {
            "type": "send_lift_log",
            "data": {
            "device": "TEST_SENSOR",
            "temperature": "42.0",
            "humidity": "88.0",
            "time": "2025-07-28 16:15",
        }
        }
    )
    print("Sent test log to lift_logs group")
    return HttpResponse("Hello, world. You're at the polls index.")

from smartlift.filters import GenericLogFilter,GatewayTimeRangeFilter
from smartlift.models import LiftEnvironmentLog, LiftControlLog, LiftDoorEventLog, LiftOccupancyLog, EnergyMeterLog, LiftFloorEventLog
from .serializers import LiftEnvironmentLogSerializer, LiftControlLogSerializer, LiftDoorEventLogSerializer, LiftOccupancyLogSerializer, EnergyMeterLogSerializer, LiftFloorEventLogSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class LiftEnvironmentLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiftEnvironmentLog.objects.all().order_by('-gateway_time')
    serializer_class = LiftEnvironmentLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenericLogFilter

class LiftControlLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiftControlLog.objects.all().order_by('-gateway_time')
    serializer_class = LiftControlLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenericLogFilter

class LiftDoorEventLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiftDoorEventLog.objects.all().order_by('-gateway_time')
    serializer_class = LiftDoorEventLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenericLogFilter

class LiftOccupancyLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiftOccupancyLog.objects.all().order_by('-gateway_time')
    serializer_class = LiftOccupancyLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenericLogFilter

class EnergyMeterLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EnergyMeterLog.objects.all().order_by('-gateway_time')
    serializer_class = EnergyMeterLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GatewayTimeRangeFilter

class LiftFloorEventLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiftFloorEventLog.objects.all().order_by('-gateway_time')
    serializer_class = LiftFloorEventLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenericLogFilter