from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
    event_type = models.CharField(max_length=100)  
    event_date = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.event_type} - {self.device.name}"
