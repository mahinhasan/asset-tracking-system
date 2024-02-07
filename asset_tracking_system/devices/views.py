
from django.shortcuts import render
from .models import Device

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devicesList.html', {'devices': devices})

def device_detail(request, device_id):
    device = Device.objects.get(pk=device_id)
    return render(request, 'deviceDetails.html', {'device': device})
