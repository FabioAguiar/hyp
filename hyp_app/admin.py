from django.contrib import admin
from .models import Peripheral, Cycle, Broker

admin.site.register(Peripheral)
admin.site.register(Cycle)
admin.site.register(Broker)