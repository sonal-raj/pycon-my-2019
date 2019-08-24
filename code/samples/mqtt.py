# Skeletal Code for MQTT Use

import time
import paho.mqtt.client as paho

#broker="broker.hivemq.com"
#broker="iot.eclipse.org"
broker = "183.83.170.228:8060"

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

# create client object client1.on_publish = on_publish 
# assign function to callback client1.connect(broker,port) 
# establish connection client1.publish("house/bulb1","on")
client= paho.Client("client-001") 
######Bind function to callback

client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages

print("subscribing ")
client.subscribe("house/bulb1")#subscribe
time.sleep(2)
print("publishing ")
client.publish("house/bulb1","on")#publish
time.sleep(4)

client.disconnect() #disconnect
client.loop_stop() #stop loop