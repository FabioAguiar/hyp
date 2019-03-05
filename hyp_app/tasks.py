from django.shortcuts import get_object_or_404
from .models import Peripheral, Cycle
from datetime import date
import datetime
from . import mqtt


def cycles_scheduler():
	today = date.today()
	now = datetime.datetime.now().time()
	cycles = Cycle.objects.all()

	for cycle in cycles:
		if(today >= cycle.start_cycle.date() and today < cycle.end_cycle.date()):
			if(now >= cycle.start_time and now < cycle.end_time):
				state = "1.0"
				peripheral_actuador(cycle.actuador_id, state)
			else:
				state = "0.0"
				peripheral_actuador(cycle.actuador_id, state)
		else:
			state = "0.0"
			peripheral_actuador(cycle.actuador_id, state)



def peripheral_actuador(peripheral, state):
    peripheral.last_record_state = state
    peripheral.save()
    mqtt.client.publish(peripheral.mqtt_topic, peripheral.last_record_state[:-2])