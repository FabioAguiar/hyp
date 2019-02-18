from django.db import models
from django.utils import timezone
from PIL import Image


#class Cicle (models.Model):
#	cicle_id = models.AutoField(primary_key=True)

class Peripheral(models.Model):
	peripheral_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, default='')
	technical_name = models.CharField(max_length=50, default='')
	topic_base = models.CharField(max_length=50, default='')
	type_peripheral = models.CharField(max_length=10, default='')		
	topic_name = models.CharField(max_length=50, default='')		
	specification = models.CharField(max_length=10, default='')
	description = models.TextField(default='')
	mqtt_topic = models.CharField(max_length=50, default='')
	is_activated = models.BooleanField(default=False)
	last_record = models.CharField(max_length=100, default='', null=True)
	last_record_state = models.CharField(max_length=10, default='')
	