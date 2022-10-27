import paho.mqtt.client as paho
import numpy as np

frecs = [0, 0, 0, 0, 0, 0, 0]
nucs = [0, 0, 0, 0, 0, 0, 0]
usos = [0, 0, 0, 0, 0, 0, 0]
mems = [0, 0, 0, 0, 0, 0, 0]
procs = ["", "", "", "", "", "", ""]

def parse(value):
    tmp_frec = value
    data = tmp_frec.split("'")
    return data[1]

def on_message(client, userdata, msg):
    averageFrec = 0
    if (msg.topic == "dafne/frec"):
        frecs[0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/frec"):
        frecs[1] = float(parse(str(msg.payload)))
    if (msg.topic == "dafne_badillo/frec"):
        frecs[2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/frec"):
        frecs[3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/frec"):
        frecs[4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/frec"):
        frecs[5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/frec"):
        frecs[6] = float(parse(str(msg.payload)))
    for i in frecs:
        averageFrec += i
    
    f_frec_min = "{:.2f}".format(np.min(frecs))
    print("Frec min.: ", str(f_frec_min))
    f_frec_avg = "{:.2f}".format(averageFrec/3)
    print("Frec avg.: ", str(f_frec_avg))
    f_frec_max = "{:.2f}".format(np.max(frecs))
    print("Frec max.: ", str(f_frec_max))
    print("---------")
    #############################################
    averageNuc = 0
    if (msg.topic == "dafne/nuc"):
        nucs[0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/nuc"):
        nucs[1] = float(parse(str(msg.payload)))
    if (msg.topic == "dafne_badillo/nuc"):
        nucs[2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/nuc"):
        nucs[3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/nuc"):
        nucs[4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/nuc"):
        nucs[5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/nuc"):
        nucs[6] = float(parse(str(msg.payload)))
    for i in nucs:
        averageNuc += i

    f_nuc_min = "{:.2f}".format(np.min(nucs))
    print("Nuc min.: ", str(f_nuc_min))
    f_nuc_avg = "{:.2f}".format(averageNuc/3)
    print("Nuc avg.: ", str(f_nuc_avg))
    f_nuc_max = "{:.2f}".format(np.max(nucs))
    print("Nuc max.: ", str(f_nuc_max))
    print("---------")
    #############################################
    averageUso = 0
    if (msg.topic == "dafne/uso"):
        usos[0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/uso"):
        usos[1] = float(parse(str(msg.payload)))
    if (msg.topic == "dafne_badillo/uso"):
        usos[2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/uso"):
        usos[3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/uso"):
        usos[4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/uso"):
        usos[5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/uso"):
        usos[6] = float(parse(str(msg.payload)))
    for i in usos:
        averageUso += i

    f_uso_min = "{:.2f}".format(np.min(usos))
    print("Uso min.: ", str(f_uso_min))
    f_uso_avg = "{:.2f}".format(averageUso/3)
    print("Uso avg.: ", str(f_uso_avg))
    f_uso_max = "{:.2f}".format(np.max(usos))
    print("Uso max.: ", str(f_uso_max))
    print("---------")
    #############################################
    averageMem = 0
    if (msg.topic == "dafne/mem"):
        mems[0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/mem"):
        mems[1] = float(parse(str(msg.payload)))
    if (msg.topic == "dafne_badillo/mem"):
        mems[2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/mem"):
        mems[3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/mem"):
        mems[4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/mem"):
        mems[5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/mem"):
        mems[6] = float(parse(str(msg.payload)))
    for i in mems:
        averageMem += i

    f_mem_min = "{:.2f}".format(np.min(mems))
    print("Mem min.: ", str(f_mem_min))
    f_mem_avg = "{:.2f}".format(averageMem/3)
    print("Mem avg.: ", str(f_mem_avg))
    f_mem_max = "{:.2f}".format(np.max(mems))
    print("Mem max.: ", str(f_mem_max))
    print("---------")
    #############################################
    if (msg.topic == "dafne/proc"):
        procs[0] = parse(str(msg.payload))
    if (msg.topic == "miles/proc"):
        procs[1] = parse(str(msg.payload))
    if (msg.topic == "dafne_badillo/proc"):
        procs[2] = parse(str(msg.payload))
    if (msg.topic == "victor/proc"):
        procs[3] = parse(str(msg.payload))
    if (msg.topic == "joseduardo/proc"):
        procs[4] = parse(str(msg.payload))
    if (msg.topic == "alonso/proc"):
        procs[5] = parse(str(msg.payload))
    if (msg.topic == "anthony/proc"):
        procs[6] = parse(str(msg.payload))

    print("Proc.: ", procs)
    print("---------")

client = paho.Client()
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("dafne/frec", qos=1)
client.subscribe("dafne/nuc", qos=1)
client.subscribe("dafne/uso", qos=1)
client.subscribe("dafne/mem", qos=1)
client.subscribe("dafne/proc", qos=1)
client.subscribe("miles/frec", qos=1)
client.subscribe("miles/nuc", qos=1)
client.subscribe("miles/uso", qos=1)
client.subscribe("miles/mem", qos=1)
client.subscribe("miles/proc", qos=1)
client.subscribe("dafne_badillo/frec", qos=1)
client.subscribe("dafne_badillo/nuc", qos=1)
client.subscribe("dafne_badillo/uso", qos=1)
client.subscribe("dafne_badillo/mem", qos=1)
client.subscribe("dafne_badillo/proc", qos=1)
client.subscribe("victor/frec", qos=1)
client.subscribe("victor/nuc", qos=1)
client.subscribe("victor/uso", qos=1)
client.subscribe("victor/mem", qos=1)
client.subscribe("victor/proc", qos=1)
client.subscribe("joseduardo/frec", qos=1)
client.subscribe("joseduardo/nuc", qos=1)
client.subscribe("joseduardo/uso", qos=1)
client.subscribe("joseduardo/mem", qos=1)
client.subscribe("joseduardo/proc", qos=1)
client.subscribe("alonso/frec", qos=1)
client.subscribe("alonso/nuc", qos=1)
client.subscribe("alonso/uso", qos=1)
client.subscribe("alonso/mem", qos=1)
client.subscribe("alonso/proc", qos=1)
client.subscribe("anthony/frec", qos=1)
client.subscribe("anthony/nuc", qos=1)
client.subscribe("anthony/uso", qos=1)
client.subscribe("anthony/mem", qos=1)
client.subscribe("anthony/proc", qos=1)
client.loop_forever()