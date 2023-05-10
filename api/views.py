from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FanSwitchSerializer
from .serializers import LightSwitchSerializer

from . import mqttserver as MQTT

MQTT.ConnectToAda()

class FanSwitchView(APIView):
    def post(self, request, format=None):
        serializer = FanSwitchSerializer(data=request.data)
        if serializer.is_valid():
            fan_switch_value = serializer.validated_data['fan_switch']
            # do something with fan_switch_value here
            MQTT.mqttClient.publish(MQTT.fanswitch, int(fan_switch_value == True))
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LightSwitchView(APIView):
    def post(self, request, format=None):
        serializer = LightSwitchSerializer(data=request.data)
        if serializer.is_valid():
            light_switch_value = serializer.validated_data['light_switch']
            # do something with fan_switch_value here
            MQTT.mqttClient.publish(MQTT.lightswitch, int(light_switch_value == True))
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def index(request):
    return render(request, 'index.html')