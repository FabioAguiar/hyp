from django.contrib import admin
from .models import Sensor, Actuator, LogDataSensor, LogDataActuator, MicrocontrollerAttributes, SensorConfiguration, ActuatorConfiguration, FilesAttachments

admin.site.register(Sensor)
admin.site.register(Actuator)
admin.site.register(LogDataSensor)
admin.site.register(LogDataActuator)
admin.site.register(MicrocontrollerAttributes)
admin.site.register(SensorConfiguration)
admin.site.register(ActuatorConfiguration)
admin.site.register(FilesAttachments)