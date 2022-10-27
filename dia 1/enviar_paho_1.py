import paho.mqtt.client as paho
from random import randint
import time
import psutil

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects

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
    listOfRunningProcess = getListOfProcessSortedByMemory()
    for elem in listOfRunningProcess[:5] :
        print(elem)
    time.sleep(30)
