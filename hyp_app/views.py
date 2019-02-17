from django.shortcuts import render, get_object_or_404
from .models import Peripheral, Sensor, Actuator, LogDataSensor, LogDataActuator, Microcontroller, SensorConfiguration, ActuatorConfiguration, FilesAttachments, MQTTLog
from django.utils import timezone
from .forms import PeripheralForm, SensorForm, ActuatorForm, MicrocontrollerForm
from django.shortcuts import redirect

def control_panel(request):
    return render(request, 'hyp_app/control_panel.html', {})

def dashboard(request):
    return render(request, 'hyp_app/dashboard.html', {})


def peripheral_edit(request, pk):
    peripheral = get_object_or_404(Peripheral, pk=pk)
    if request.method == "POST":
        form = PeripheralForm(request.POST, instance=peripheral)
        print(form)
        if form.is_valid():
            peripheral = form.save(commit=False)
            peripheral.author = request.user
            peripheral.save()
            return redirect('peripheral_detail', pk=peripheral.pk)
    else:
        form = PeripheralForm(instance=peripheral)
    return render(request, 'hyp_app/peripheral_edit.html', {'peripheral': peripheral})    



def peripheral_detail(request, pk):
    print("peripheral_detail")    
    peripheral = get_object_or_404(Peripheral, pk=pk)
    return render(request, 'hyp_app/peripheral_detail.html', {'peripheral': peripheral})




def peripheral_new(request):
    if request.method == "POST":
        form = PeripheralForm(request.POST)
        if form.is_valid():
            peripheral = form.save(commit=False)
            peripheral.author = request.user
            peripheral.save()
            return redirect('peripheral_detail', pk=peripheral.pk)
    else:
        form = PeripheralForm()
        
    return render(request, 'hyp_app/peripheral_new.html', {'form': form})


#def peripheral_edit(request, pk):
#    print("AEW")
#    peripheral = get_object_or_404(Peripheral, pk=pk)
#    if request.method == "POST":
#        form = PeripheralForm(request.POST, instance=peripheral)
#        if form.is_valid():
#            peripheral = form.save(commit=False)
#            peripheral.author = request.user
#            #peripheral.published_date = timezone.now()
#            peripheral.save()
#            return redirect('peripheral_detail', pk=peripheral.pk)
#    else:
#        form = PeripheralForm(instance=peripheral)
#    return render(request, 'hyp_app/detail_peripheral.html', {'form': form})




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
    sensors = Sensor.objects.all()
    return render(request, 'hyp_app/sensor_list.html', {'sensors': sensors})



def actuator_detail(request, pk):
    actuator = get_object_or_404(Actuator, pk=pk)
    return render(request, 'hyp_app/actuator_detail.html', {'actuator': actuator})


def actuator_new(request):
    if request.method == "POST":
        form = ActuatorForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            actuator = form.save(commit=False)
            actuator.author = request.user
            actuator.published_date = timezone.now()
            actuator.save()
            return redirect('actuator_detail', pk=actuator.pk)
    else:
        form = ActuatorForm()
    return render(request, 'hyp_app/actuator_edit.html', {'form': form})

def actuator_edit(request, pk):
    actuator = get_object_or_404(Actuator, pk=pk)
    if request.method == "POST":
        form = ActuatorForm(request.POST, instance=actuator)
        if form.is_valid():
            actuator = form.save(commit=False)
            actuator.author = request.user
            actuator.published_date = timezone.now()
            actuator.save()
            return redirect('actuator_detail', pk=actuator.pk)
    else:
        form = ActuatorForm(instance=actuator)
    return render(request, 'hyp_app/actuator_edit.html', {'form': form})


def actuator_list(request):
    actuators = Actuator.objects.all()
    return render(request, 'hyp_app/actuator_list.html', {'actuators': actuators})



def microcontroller_detail(request, pk):
    microcontroller = get_object_or_404(Microcontroller, pk=pk)
    return render(request, 'hyp_app/microcontroller_detail.html', {'microcontroller': microcontroller})


def microcontroller_new(request):
    if request.method == "POST":
        form = MicrocontrollerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            microcontroller = form.save(commit=False)
            microcontroller.author = request.user
            microcontroller.published_date = timezone.now()
            microcontroller.save()
            return redirect('microcontroller_detail', pk=microcontroller.pk)
    else:
        form = MicrocontrollerForm()
    return render(request, 'hyp_app/microcontroller_edit.html', {'form': form})

def microcontroller_edit(request, pk):
    microcontroller = get_object_or_404(Microcontroller, pk=pk)
    if request.method == "POST":
        form = MicrocontrollerForm(request.POST, instance=microcontroller)
        if form.is_valid():
            microcontroller = form.save(commit=False)
            microcontroller.author = request.user
            microcontroller.published_date = timezone.now()
            microcontroller.save()
            return redirect('microcontroller_detail', pk=microcontroller.pk)
    else:
        form = MicrocontrollerForm(instance=microcontroller)
    return render(request, 'hyp_app/microcontroller_edit.html', {'form': form})


def microcontroller_list(request):
    microcontrollers = Microcontroller.objects.all()
    return render(request, 'hyp_app/microcontroller_list.html', {'microcontrollers': microcontrollers})