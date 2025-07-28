from rest_framework import serializers
from .models import (
    LiftEnvironmentLog,
    LiftControlLog,
    LiftDoorEventLog,
    LiftOccupancyLog,
    EnergyMeterLog,
    LiftFloorEventLog
)

class LiftEnvironmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftEnvironmentLog
        fields = '__all__'

class LiftControlLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftControlLog
        fields = '__all__'

class LiftDoorEventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftDoorEventLog
        fields = '__all__'

class LiftOccupancyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftOccupancyLog
        fields = '__all__'

class EnergyMeterLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyMeterLog
        fields = '__all__'

class LiftFloorEventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftFloorEventLog
        fields = '__all__'
