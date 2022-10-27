    
import time
from random import randint
import psutil
import pyrebase


from dotenv import load_dotenv
import os

load_dotenv()

config = {
  "apiKey" :  os.getenv('API_KEY'),
  "authDomain" : os.getenv('AUTH'),
  "databaseURL" : os.getenv('DB_URL'),
  "projectId" : os.getenv('PID'),
  "storageBucket" : os.getenv('SB'),
  "messagingSenderId" : os.getenv('MID'),
  "appId" : os.getenv('APP_ID')
}


config1 = {
  "apiKey" :  os.getenv('API_KEY_1'),
  "authDomain" : os.getenv('AUTH_1'),
  "databaseURL" : os.getenv('DB_URL_1'),
  "projectId" : os.getenv('PID_1'),
  "storageBucket" : os.getenv('SB_1'),
  "messagingSenderId" : os.getenv('MID_1'),
  "appId" : os.getenv('APP_ID_1')
}

config2 = {
  "apiKey" :  os.getenv('API_KEY_2'),
  "authDomain" : os.getenv('AUTH_2'),
  "databaseURL" : os.getenv('DB_URL_2'),
  "projectId" : os.getenv('PID_2'),
  "storageBucket" : os.getenv('SB_2'),
  "messagingSenderId" : os.getenv('MID_2'),
  "appId" : os.getenv('APP_ID_2')
}


config3 = {
  "apiKey" :  os.getenv('API_KEY_3'),
  "authDomain" : os.getenv('AUTH_3'),
  "databaseURL" : os.getenv('DB_URL_3'),
  "projectId" : os.getenv('PID_3'),
  "storageBucket" : os.getenv('SB_3'),
  "messagingSenderId" : os.getenv('MID_3'),
  "appId" : os.getenv('APP_ID_3')
}


config4 = {
  "apiKey" :  os.getenv('API_KEY_4'),
  "authDomain" : os.getenv('AUTH_4'),
  "databaseURL" : os.getenv('DB_URL_4'),
  "projectId" : os.getenv('PID_4'),
  "storageBucket" : os.getenv('SB_4'),
  "messagingSenderId" : os.getenv('MID_4'),
  "appId" : os.getenv('APP_ID_4')
}

config5 = {
  "apiKey" :  os.getenv('API_KEY_5'),
  "authDomain" : os.getenv('AUTH_5'),
  "databaseURL" : os.getenv('DB_URL_5'),
  "projectId" : os.getenv('PID_5'),
  "storageBucket" : os.getenv('SB_5'),
  "messagingSenderId" : os.getenv('MID_5'),
  "appId" : os.getenv('APP_ID_5')
  
}

config6 = {
  "apiKey" :  os.getenv('API_KEY_6'),
  "authDomain" : os.getenv('AUTH_6'),
  "databaseURL" : os.getenv('DB_URL_6'),
  "projectId" : os.getenv('PID_6'),
  "storageBucket" : os.getenv('SB_6'),
  "messagingSenderId" : os.getenv('MID_6'),
  "appId" : os.getenv('APP_ID_6')
}






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





listOfRunningProcess = getListOfProcessSortedByMemory()
tmp_proc = str(listOfRunningProcess[0])
i = tmp_proc.find("'name':")+ 9
f = tmp_proc.index("'",i)
tmp_proc = tmp_proc[i:f].strip()



while True:
    #create authetication
    firebase = pyrebase.initialize_app(config)
    firebase1 = pyrebase.initialize_app(config1)
    firebase2= pyrebase.initialize_app(config2)
    firebase3 = pyrebase.initialize_app(config3)
    firebase4 = pyrebase.initialize_app(config4)
    firebase5 = pyrebase.initialize_app(config5)
    firebase6 = pyrebase.initialize_app(config6)
    #accesing database in firebase
    db = firebase.database()
    db1 = firebase1.database()
    db2 = firebase2.database()
    db3 = firebase3.database()
    db4 = firebase4.database()
    db5 = firebase5.database()
    db6 = firebase6.database()

    data = {"nuc": psutil.cpu_count(),
    "frec":psutil.cpu_freq()[0],
    "uso":psutil.cpu_percent(4),
    "mem":psutil.virtual_memory()[0],
    "proc":tmp_proc
    }
    db.child("users").child("Alan").push(data)
    db1.child("users").child("Alan").push(data)
    db2.child("users").child("Alan").push(data)
    db3.child("users").child("Alan").push(data)
    db4.child("users").child("Alan").push(data)
    db5.child("users").child("Alan").push(data)
    db6.child("users").child("Alan").push(data)

    print("Data added to real time database ")
    time.sleep(120)



