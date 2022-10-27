import paho.mqtt.client as paho
import time
import psutil

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

#Parser from Moises Milles 
def parseProc():
    tmp_proc = str(proc[0])
    i = tmp_proc.find("'name':") + 9
    f = tmp_proc.index("'", i)
    tmp_proc = tmp_proc[i:f].strip()
    return tmp_proc

client = paho.Client()
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()
proc = getListOfProcessSortedByMemory()

while True:
    proc = getListOfProcessSortedByMemory()
    (rc, att) = client.publish("Alan/frec", str(psutil.cpu_freq()[0]), qos = 1)
    (rc, att) = client.publish("Alan/nuc", str(psutil.cpu_count()), qos = 1)
    (rc, att) = client.publish("Alan/uso", str(psutil.cpu_percent(4)), qos = 1)
    (rc, att) = client.publish("Alan/mem", str(psutil.virtual_memory()[0]), qos = 1)
    (rc, att) = client.publish("Alan/proc", str(parseProc()), qos = 1)
    print("frec: ", psutil.cpu_freq()[0])
    print("nuc: ", psutil.cpu_count())
    print("uso: ", psutil.cpu_percent(4))
    print("mem: ", psutil.virtual_memory()[0])
    print("proc: ", parseProc())
    time.sleep(30)