import os
import sys
import paho.mqtt.client as mqtt
import time
import random
import json

MQTT_SERVER = "io.adafruit.com"
MQTT_PORT = 1883
MQTT_USERNAME = "hungnguyen2509"
MQTT_PASSWORD = "aio_yUCz712mbnGye5IZLvnaIW4qthtf"
MQTT_FEEDS= ['projectxt2.fanswitch', 'projectxt2.lightswitch', 'projectxt2.temperature', 'projectxt2.detectresult', 'projectxt2.detectname']
PATH = 'hungnguyen2509/feeds/'

mqttClient = mqtt.Client()

fanswitch = PATH + MQTT_FEEDS[0]
lightswitch = PATH + MQTT_FEEDS[1]
temperaturesensor = PATH + MQTT_FEEDS[2]
detectresult = PATH + MQTT_FEEDS[3]
detectname = PATH + MQTT_FEEDS[4]

temper_val = 0
detect_res = 0
detect_name = "None"

def mqtt_connected(client, userdata, flags, rc):
    for feed in MQTT_FEEDS:
        client.subscribe(PATH + feed)

    print("Connected succesfully!!")


def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def mqtt_message(client, userdata, msg):
    if(msg.topic == temperaturesensor):
        decoded_message=str(msg.payload.decode("utf-8"))
        message = json.loads(decoded_message)
        global temper_val
        temper_val = message

    if(msg.topic == detectname):
        decoded_message= msg.payload.decode("utf-8")
        global detect_name
        detect_name = decoded_message

    if(msg.topic == detectresult):
        decoded_message=str(msg.payload.decode("utf-8"))
        message = json.loads(decoded_message)
        if message == 2:
            global detect_res
            detect_res = 1

def ConnectToAda():
        #Register mqtt events
    mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    mqttClient.connect(MQTT_SERVER, MQTT_PORT, 60)

    #Register mqtt events
    mqttClient.on_connect = mqtt_connected
    mqttClient.on_disconnect = disconnected
    mqttClient.on_subscribe = mqtt_subscribed
    mqttClient.on_message = mqtt_message

    mqttClient.loop_start()