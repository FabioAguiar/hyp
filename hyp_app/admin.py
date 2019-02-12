from django.contrib import admin
from .models import Peripheral, Sensor, Actuator, LogDataSensor, LogDataActuator, Microcontroller, SensorConfiguration, ActuatorConfiguration, FilesAttachments

admin.site.register(Peripheral)
admin.site.register(Sensor)
admin.site.register(Actuator)
admin.site.register(LogDataSensor)
admin.site.register(LogDataActuator)
admin.site.register(Microcontroller)
admin.site.register(SensorConfiguration)
admin.site.register(ActuatorConfiguration)
admin.site.register(FilesAttachments)
