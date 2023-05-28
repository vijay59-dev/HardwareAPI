import psutil
import platform
import json
from datetime import datetime

def Disk_Function():

    #Return all mounted disk partitions as a list of named tuples
    disk_partitions = psutil.disk_partitions
    system = {'diskDetails': []}

    for p in disk_partitions(all=True):
        try:
            usage = psutil.disk_usage(p.mountpoint)
            mountpoint = p.mountpoint
            total = str(float(usage.total) / (2 ** 30)) + " GiB"
            used = str(float(usage.used) / (2 ** 30)) + " GiB"
            system['diskDetails'].append({
                'mountpoint': mountpoint,
                'total': total,
                'used': used,
                'fileSystem': p[2],
                'permission': p[3]
                })
        except PermissionError and OSError:
            continue

    #Return disk usage statistics including total used and free space expressed in bytes, plus the percentage usage
    total = int()
    used = int()
    free = int()

    for disk in psutil.disk_partitions():
        if disk.fstype:
            total += int(psutil.disk_usage(disk.mountpoint).total)
            used += int(psutil.disk_usage(disk.mountpoint).used)
            free += int(psutil.disk_usage(disk.mountpoint).free)

    disk_usage = {'totalDiskSpace': str(round(total / (1024.0 ** 3), 4)) + " GiB",
                  'usedDiskSpace': str(round(used / (1024.0 ** 3), 4)) + " GiB",
                  'freeDiskSpace': str(round(free / (1024.0 ** 3), 4)) + " GiB"}




    #Return system-wide disk I/O statistics as a named tuple
    disk_io_counters = psutil.disk_io_counters(perdisk=False, nowrap=True)
    ioCounters = {'readCount': disk_io_counters[0],
                  'writeCount': disk_io_counters[1],
                  'readbytes': disk_io_counters[2],
                  'writebytes': disk_io_counters[3],
                  'readTime': disk_io_counters[4],
                  'writeTime': disk_io_counters[5]}


    diskFunction= {"diskPartitions": system['diskDetails'],
                   "diskUsage": disk_usage,
                   "diskIOCounters": ioCounters}
    return diskFunction
    
Disk_Function()