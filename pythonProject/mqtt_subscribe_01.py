#https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4

import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("TEMPERATURE")
client.on_message=on_message

time.sleep(30)
client.loop_stop()