from django.shortcuts import render #pip install django djangorestframework
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FanSwitchSerializer
from .serializers import LightSwitchSerializer

from . import mqttserver as MQTT
# connect to adafruit server
MQTT.ConnectToAda()

# send data received from switch to the server
class FanSwitchView(APIView):
    def post(self, request, format=None):
        serializer = FanSwitchSerializer(data=request.data)
        if serializer.is_valid() and MQTT.detect_res == 1:
            fan_switch_value = serializer.validated_data['fan_switch']
            MQTT.mqttClient.publish(MQTT.fanswitch, int(fan_switch_value == True))
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LightSwitchView(APIView):
    def post(self, request, format=None):
        serializer = LightSwitchSerializer(data=request.data)
        if serializer.is_valid() and MQTT.detect_res == 1:
            light_switch_value = serializer.validated_data['light_switch']
            MQTT.mqttClient.publish(MQTT.lightswitch, int(light_switch_value == True))
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TemperatureView(APIView):
    def get(self, request, format=None):
        current_temperature = MQTT.temper_val
        return Response({'temperature': current_temperature})
    
class DetectView(APIView):
    def get(self, request, format=None):
        current_status = "Allow" if MQTT.detect_res == 1 else "Block"
        return Response({'detectstatus': current_status})
    
class NameView(APIView):
    def get(self, request, format=None):
        current_name = MQTT.detect_name
        return Response({'detectname': current_name})
    
def index(request):
    return render(request, 'index.html')