import psutil
import platform
import json
from datetime import datetime

def SystemInformation():
    systemInformation = {}
    uname = platform.uname()
    system = json.dumps(uname.system)
    node_name = json.dumps(uname.node)
    release = json.dumps(uname.release)
    version = json.dumps(uname.version)
    machine = json.dumps(uname.machine)
    proc = json.dumps(uname.processor)
    systemInformation = {"system": system, "nodeName": node_name, "release": release, "version": version, "machine": machine,
            "processor": proc}
    return systemInformation
    
def CPU_Function():
    # number of cores
    physical_cores = json.dumps(psutil.cpu_count(logical=False))
    total_cores = json.dumps(psutil.cpu_count(logical=True))
    cpufrequency = json.dumps(psutil.cpu_freq())
    # CPU usage per core
    cpu_xcore = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        cpu_xcore.append(json.dumps(percentage))
    #CPU total usage
    cpu_total = json.dumps(psutil.cpu_percent())
    cpuFunction = {"physicalCores": physical_cores, "totalCores":total_cores, "cpuFrequency": cpufrequency,
                   "cpuTotal":cpu_total, "cpuPerCore":cpu_xcore}
    return cpuFunction

def cpuDetails():
    cpudetails = {"systemInformation": SystemInformation(), "cpuFunction": CPU_Function()}
    return cpudetails