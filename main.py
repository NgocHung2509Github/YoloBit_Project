import sys
import time
import paho.mqtt.client as mqtt
MQTT_SERVER = "io.adafruit.com"
MQTT_PORT = 1883
MQTT_USERNAME = "HauNg"
MQTT_PASSWORD = "aio_GFpb34Vx9muBcclCNV8aqqSMt4j9"
MQTT_FEED= "HauNg/feeds/nutnhan1"

def mqtt_connected(client, userdata, flags, rc):
    client.subscribe(MQTT_FEED)
    print("Connected succesfully!!")


def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)


#Register mqtt events
mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, 1883, 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_disconnect = disconnected
mqttClient.on_subscribe = mqtt_subscribed


mqttClient.loop_start()
counter = 0


while True:
    counter=counter+1
    if counter==5:
        mqttClient.publish(MQTT_FEED, 1)
        print("Published!")
    if counter==10:
        mqttClient.publish(MQTT_FEED, 0)
        print("Published!")
        counter=0
    time.sleep(1)