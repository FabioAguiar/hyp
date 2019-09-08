from django.db import models
from PIL import Image


class User(models.Model):
	name = models.CharField(max_length=50, default='')
	email = models.CharField(max_length=50, default='')
	passwd = models.CharField(max_length=50, default='')


class Login(models.Model):
	email = models.CharField(max_length=50, default='')
	passwd = models.CharField(max_length=50, default='')

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
	data_metric = models.CharField(max_length=10, default='')
	firebase_id = models.CharField(max_length=40, default='')
	

class Cycle(models.Model):
	cycle_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, default='')
	actuador_id = models.ForeignKey(Peripheral, default=None, on_delete=models.CASCADE)
	is_activated = models.BooleanField(default=False)
	start_time = models.TimeField(blank=True, null=True)
	end_time = models.TimeField(blank=True, null=True)
	start_cycle = models.DateTimeField(blank=True, null=True)
	end_cycle = models.DateTimeField(blank=True, null=True)


class Broker(models.Model):
	broker_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, default='')
	port = models.IntegerField()
	keep_alive = models.IntegerField()
	user_name = models.CharField(max_length=50, default='')
	passwd = models.CharField(max_length=50, default='')
	is_activated = models.BooleanField(default=False)