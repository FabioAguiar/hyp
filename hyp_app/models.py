from django.db import models
from django.utils import timezone
from PIL import Image


#class Cicle (models.Model):
#	cicle_id = models.AutoField(primary_key=True)


class Sensor(models.Model):
	sensor_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, default='')
	technical_name = models.CharField(max_length=50, default='')
	type_signal = models.CharField(max_length=10, default='')
	lib_code = models.CharField(max_length=10, default='')
	description = models.TextField(default='')
	digital_ports_quant = models.CharField(max_length=2, default='')
	analog_ports_quant = models.CharField(max_length=2, default='')	
	is_activated = models.BooleanField(default=False)
	sensor_photo = models.FileField(upload_to='sensor_photo', null='True', blank='True')
	sensor_document_1 = models.FileField(upload_to='sensor_document_1', null='True', blank='True')
	sensor_document_2 = models.FileField(upload_to='sensor_document_2', null='True', blank='True')
	sensor_document_3 = models.FileField(upload_to='sensor_document_3', null='True', blank='True')
	published_date = models.DateTimeField(blank=True, null=True)
	#state_cicle1 = models.BooleanField(default=False)
	#time_cicle1_begin = models.TimeField(blank=True, null=True)
	#time_cicle1_end = models.TimeField(blank=True, null=True)
	#state_cicle2 = models.BooleanField(default=False)	
	#time_cicle2_begin = models.TimeField(blank=True, null=True)
	#time_cicle2_end = models.TimeField(blank=True, null=True)
	#date_time_create = models.DateTimeField(blank=True, null=True)
	
	def date_time(self):
		self.date_time_create = timezone.now()
		self.save()


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name
	
		
class Actuator(models.Model):
    actuator_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    technical_name = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=100, default='')
    is_activated = models.BooleanField(default=False)
    actuator_photo = models.FileField(upload_to='actuator_photo', null='True', blank='True')	
    actuator_document_1 = models.FileField(upload_to='actuator_document_1', null='True', blank='True')
    actuator_document_2 = models.FileField(upload_to='actuator_document_2', null='True', blank='True')
    actuator_document_3 = models.FileField(upload_to='actuator_document_3', null='True', blank='True')

    def __str__(self):
        return self.name

class Microcontroller(models.Model):
	mc_id = models.AutoField(primary_key=True)
	type_board = models.CharField(max_length=30, default='')
	board_name = models.CharField(max_length=30, default='')
	description = models.TextField(max_length=100, default='')
	digital_ports = models.CharField(max_length=1000, default='')
	number_digital_ports = models.CharField(max_length=2, default='')
	pwm_ports =  models.CharField(max_length=100, default='')
	number_pwm_ports = models.CharField(max_length=2, default='')
	analog_ports = models.CharField(max_length=100, default='')
	number_analog_ports = models.CharField(max_length=2, default='')
	microcontroller_photo = models.FileField(upload_to='actuator_photo', null='True', blank='True')
	is_activated = models.BooleanField(default=False)
	#rx_tx_ports =  models.CharField(max_length=100, default='')
	#number_rx_tx_ports =  models.CharField(max_length=2, default='')
	#sda_scl_ports =  models.CharField(max_length=100, default='')
	#number_sda_scl_ports =  models.CharField(max_length=2, default='')

		
class LogDataSensor(models.Model): 
	log_id = models.AutoField(primary_key=True)
	sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=0)
	register1 = models.CharField(max_length=25, default='')
	register1_measure = models.CharField(max_length=20, default='')
	register2 = models.CharField(max_length=25, default='')	
	register2_measure_measure = models.CharField(max_length=20, default='')
	register3 = models.CharField(max_length=25, default='')
	register3_measure = models.CharField(max_length=20, default='')	
	date_time_data_log = models.DateTimeField(default=timezone.now)
	
	
class LogDataActuator(models.Model):
	log_id = models.AutoField(primary_key=True)
	actuator_id = models.ForeignKey(Actuator, on_delete=models.CASCADE, default=0)
	is_active = models.BooleanField(default=False)		
	date_time_data_log = models.DateTimeField(default=timezone.now)
	
	
class SensorConfiguration(models.Model):
	sensor_config_id = models.AutoField(primary_key=True)
	sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=0)
	digital_port1 = models.CharField(max_length=10, default='')
	description_digital_port1 = models.CharField(max_length=10, default='')
	mode_digital_port1 = models.CharField(max_length=10, default='')
	digital_port2 = models.CharField(max_length=10, default='')
	description_digital_port2 = models.CharField(max_length=10, default='')
	mode_digital_port2 = models.CharField(max_length=10, default='')	
	digital_port3 = models.CharField(max_length=10, default='')
	description_digital_port3 = models.CharField(max_length=10, default='')
	mode_digital_port3 = models.CharField(max_length=10, default='')	
	analog_port1 = models.CharField(max_length=10, default='')
	description_analog_port1 = models.CharField(max_length=10, default='')
	mode_analog_port1 = models.CharField(max_length=10, default='')
	analog_port2 = models.CharField(max_length=10, default='')
	description_analog_port2 = models.CharField(max_length=10, default='')
	mode_analog_port2 = models.CharField(max_length=10, default='')	
	number_ports_digital = models.IntegerField()
	number_ports_analog = models.IntegerField()
	
class ActuatorConfiguration(models.Model):
	actuator_config_id = models.AutoField(primary_key=True)
	actuator_id = models.ForeignKey(Actuator, on_delete=models.CASCADE, default=0)
	digital_port1 = models.CharField(max_length=10, default='')
	description_digital_port1 = models.CharField(max_length=10, default='')	
	digital_port2 = models.CharField(max_length=10, default='')
	description_digital_port2 = models.CharField(max_length=10, default='')	
	digital_port3 = models.CharField(max_length=10, default='')
	description_digital_port3 = models.CharField(max_length=10, default='')	
	digital_port4 = models.CharField(max_length=10, default='')
	description_digital_port4 = models.CharField(max_length=10, default='')	
	digital_port5 = models.CharField(max_length=10, default='')
	description_digital_port5 = models.CharField(max_length=10, default='')	
	digital_port6 = models.CharField(max_length=10, default='')
	description_digital_port6 = models.CharField(max_length=10, default='')	
	
class FilesAttachments(models.Model):
	font_file_id = models.CharField(max_length=10, default='')
	files_attachments = models.BinaryField(blank=True, editable=False)