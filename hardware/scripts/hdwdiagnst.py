import psutil
import json
from datetime import datetime
 
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
  
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def batteryDetails():
    battery = psutil.sensors_battery()
    batteryDetails = {}
    batteryDetails["charge"] = json.dumps(str(int(battery.percent))+"%")
    batteryDetails["timeleft"]  = json.dumps(secs2hours(battery.secsleft))
    batteryDetails["plugged"] = json.dumps(str(battery.power_plugged))
    return(batteryDetails)

def ramDetails():
    ram = psutil.virtual_memory()
    ramDetails = {}
    ramDetails["total"] = json.dumps(get_size(ram.total))
    ramDetails["available"] = json.dumps(get_size(ram.available))
    ramDetails["used"] = json.dumps(get_size(ram.used))
    ramDetails["percent"] = json.dumps(str(ram.percent)+"%")
    return(ramDetails)
batteryDetails()
