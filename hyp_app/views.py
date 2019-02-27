from django.shortcuts import render, get_object_or_404
from .models import Peripheral, Cycle
from django.utils import timezone
from .forms import PeripheralForm, CycleForm
from django.shortcuts import redirect
from . import mqtt

def dashboard(request):
    peripherals = Peripheral.objects.all()
    return render(request, 'hyp_app/dashboard.html', {'peripherals': peripherals})

def weather_station(request):
    return render(request, 'hyp_app/weather_station.html', { })

def control_panel(request):
    return render(request, 'hyp_app/control_panel.html', {})


def peripheral_actuador(request, pk):
    peripherals = Peripheral.objects.all()    
    peripheral = Peripheral.objects.get(pk=pk)

    if peripheral.last_record_state == "1.0":
        peripheral.last_record_state = "0.0"
    else:
        peripheral.last_record_state = "1.0"

    peripheral.author = request.user
    peripheral.save()
    mqtt.client.publish(peripheral.mqtt_topic, peripheral.last_record_state[:-2])

    return render(request, 'hyp_app/dashboard.html', {'peripherals': peripherals})


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

def peripheral_detail(request, pk): 
    peripheral = get_object_or_404(Peripheral, pk=pk)

    if request.method == "POST":
        form = PeripheralForm(request.POST, instance=peripheral)
        if form.is_valid():
            peripheral = form.save(commit=False)
            peripheral.author = request.user
            peripheral.save()
            return redirect('peripheral_detail', pk=peripheral.pk)
    else:
        form = PeripheralForm(instance=peripheral)
        form.pk = pk
        print(form.pk)

    return render(request, 'hyp_app/peripheral_detail.html', {'form': form})    

def peripheral_edit(request, pk):
    peripheral = get_object_or_404(Peripheral, pk=pk)
    if request.method == "POST":
        form = PeripheralForm(request.POST, instance=peripheral)
        if form.is_valid():
            peripheral = form.save(commit=False)
            peripheral.author = request.user
            peripheral.save()
            return redirect('peripheral_detail', pk=peripheral.pk)
    else:
        form = PeripheralForm(instance=peripheral)
    return render(request, 'hyp_app/peripheral_edit.html', {'peripheral': peripheral})    


def peripheral_remove(request, pk):
    peripheral = get_object_or_404(Peripheral, pk=pk)
    peripheral.delete()
    return redirect('peripheral_datatable')

def peripheral_list(request):
    peripherals = Peripheral.objects.all()
    return render(request, 'hyp_app/peripheral_datatable.html', {'peripherals': peripherals})


def cycle_new(request):
    if request.method == "POST":
        form = CycleForm(request.POST)
        if form.is_valid():
            cycle = form.save(commit=False)
            cycle.author = request.user
            cycle.save()
            return redirect('cycle_detail', pk=cycle.pk)
    else:
        form = CycleForm()
        
    return render(request, 'hyp_app/cycle_new.html', {'form': form})

def cycle_detail(request, pk): 
    cycle = get_object_or_404(Cycle, pk=pk)
    
    if request.method == "POST":
        form = CycleForm(request.POST, instance=cycle)
        if form.is_valid():
            cycle = form.save(commit=False)
            cycle.author = request.user
            cycle.save()
            return redirect('cycle_detail', pk=cycle.pk)
    else:
        form = CycleForm(instance=cycle)
        form.pk = pk
    
    return render(request, 'hyp_app/cycle_detail.html', {'form': form})

def cycle_remove(request, pk):
    cycle = get_object_or_404(Cycle, pk=pk)
    cycle.delete()
    return redirect('cycle_datatable')

def cycle_list(request):
    cycles = Cycle.objects.all()
    return render(request, 'hyp_app/cycle_datatable.html', {'cycles': cycles})