import os
import sys
import paho.mqtt.client as mqtt
import time
import random

MQTT_SERVER = "io.adafruit.com"
MQTT_PORT = 1883
MQTT_USERNAME = "hungnguyen2509"
MQTT_PASSWORD = "aio_ZSPd06WPDtWRjNM6AJYVNgLwEukD"
MQTT_FEEDS= ['projectxt2.fanswitch', 'projectxt2.lightswitch']
PATH = 'hungnguyen2509/feeds/'


def mqtt_connected(client, userdata, flags, rc):
    for feed in MQTT_FEEDS:
        client.subscribe(PATH + feed)

    print("Connected succesfully!!")


def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

    #Register mqtt events
mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, MQTT_PORT, 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_disconnect = disconnected
mqttClient.on_subscribe = mqtt_subscribed


mqttClient.loop_start()

fanswitch = PATH + MQTT_FEEDS[0]
lightswitch = PATH + MQTT_FEEDS[1]

fanswitch_value = 1

count=5
while True:
    counter = counter - 1
    if counter<=0:
        counter=5
        mqttClient.publish(fanswitch, fanswitch_value)
    time.sleep(1)