import paho.mqtt.client as paho
from random import randint
import time
import psutil

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
#client.username_pw_set("etorresr", "G4t0")
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    temperature = randint(1,30)
    (rc, mid) = client.publish("encyclopedia/temperature",
    str(temperature), qos=1)
    print(temperature)
    print('The CPU usage is: ', psutil.cpu_percent(4))
    print("Number of cores in system", psutil.cpu_count())
    print("CPU Statistics", psutil.cpu_stats())
    print("CPU frequency", psutil.cpu_freq())
    print("CPU load average 1, 5, 15 minutes", psutil.getloadavg())
    print(psutil.virtual_memory())
    print(psutil.sensors_battery())
    time.sleep(30)
