from rest_framework import serializers

class FanSwitchSerializer(serializers.Serializer):
    fan_switch = serializers.BooleanField()

class LightSwitchSerializer(serializers.Serializer):
    light_switch = serializers.BooleanField()
