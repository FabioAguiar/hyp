from django.shortcuts import get_object_or_404
from .models import Peripheral, Cycle
from datetime import date

def test():
	today = date.today()
	cycles = Cycle.objects.all()

	for cycle in cycles:
		if(today >= cycle.start_cycle.date() and today < cycle.end_cycle.date()):
			print("HOJE")
		#print(cycle.start_cycle.date())
		#print(cycle.title)
		#print(cycle.start_cycle)
