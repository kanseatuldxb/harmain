from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *


router = DefaultRouter()
router.register(r'environment', LiftEnvironmentLogViewSet)
router.register(r'control', LiftControlLogViewSet)
router.register(r'door', LiftDoorEventLogViewSet)
router.register(r'occupancy', LiftOccupancyLogViewSet)
router.register(r'energy', EnergyMeterLogViewSet)
router.register(r'floor', LiftFloorEventLogViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]