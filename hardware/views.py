import json
from django.shortcuts import render
from django.http import HttpResponse
from .scripts import proyecto_cpu, hard_disk, hdwdiagnst

from . import templates

# Create your views here.

def home(request):
    return render(request, 'hardware.html')


def cpuDetails(request):
    cpuDetails = proyecto_cpu.cpuDetails()
    return render(request, 'hardware.html', {'cpuDetails': cpuDetails})


def ramDetails(request):
    ramDetails = hdwdiagnst.ramDetails()
    return render(request, 'hardware.html', {'ramDetails': ramDetails})


def diskDetails(request):
    diskDetails = hard_disk.Disk_Function()
    return render(request, 'hardware.html', {'diskDetails': diskDetails})


def batteryDetails(request):
    batteryDetails = hdwdiagnst.batteryDetails()
    return render(request, 'hardware.html', {'batteryDetails': batteryDetails})