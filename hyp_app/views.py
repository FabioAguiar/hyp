from django.shortcuts import render, get_object_or_404
from .models import Sensor, Actuator, LogDataSensor, LogDataActuator, MicrocontrollerAttributes, SensorConfiguration, ActuatorConfiguration, FilesAttachments
from django.utils import timezone
from .forms import SensorForm
from django.shortcuts import redirect


def dashboard(request):
	return render(request, 'hyp_app/dashboard.html', {})

def sensor_detail(request, pk):
	sensor = get_object_or_404(Sensor, pk=pk)
	return render(request, 'hyp_app/sensor_detail.html', {'sensor': sensor})


def sensor_new(request):
    if request.method == "POST":
        form = SensorForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            sensor = form.save(commit=False)
            sensor.author = request.user
            sensor.published_date = timezone.now()
            sensor.save()
            return redirect('sensor_detail', pk=sensor.pk)
    else:
        form = SensorForm()
    return render(request, 'hyp_app/sensor_edit.html', {'form': form})

def sensor_edit(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == "POST":
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            sensor = form.save(commit=False)
            sensor.author = request.user
            sensor.published_date = timezone.now()
            sensor.save()
            return redirect('sensor_detail', pk=sensor.pk)
    else:
        form = SensorForm(instance=sensor)
    return render(request, 'hyp_app/sensor_edit.html', {'form': form})


def sensor_list(request):
    sensors = Sensor.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hyp_app/sensor_list.html', {'sensors': sensors})