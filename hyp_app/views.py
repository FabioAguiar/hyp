from django.shortcuts import render, get_object_or_404
from .models import Login, Peripheral, Cycle, Broker
from .forms import PeripheralForm, CycleForm, BrokerForm, LoginForm
from django.shortcuts import redirect
from . import mqtt
import time

import pyrebase
from django.contrib import auth
config = {
    'apiKey': "AIzaSyBse-xWFqcWnnMSqvJsmt1MP7ILOAHw7jw",
    'authDomain': "hypmobile-51803.firebaseapp.com",
    'databaseURL': "https://hypmobile-51803.firebaseio.com",
    'projectId': "hypmobile-51803",
    'storageBucket': "hypmobile-51803.appspot.com",
    #'messagingSenderId': "579985583952"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def signIn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            passwd = request.POST.get('passwd')

            print(email)
            print(passwd)
            try:
                user = auth.sign_in_with_email_and_password(email, passwd)
            except:
                message="invalid credentials"
                return render(request,'hyp_app/login.html',{'messg':message})

            peripherals = Peripheral.objects.all()

            print(user['idToken'])
            session_id=user['idToken']
            request.session['uid']=str(session_id)
            return render(request, 'hyp_app/dashboard.html', {'peripherals': peripherals})
    else:
        form = LoginForm()
    
    return render(request, 'hyp_app/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return render(request,'hyp_app/login.html')


def dashboard(request):
    peripherals = Peripheral.objects.all()
    return render(request, 'hyp_app/dashboard.html', {'peripherals': peripherals})

def weather_station(request):
    return render(request, 'hyp_app/weather_station.html', { })

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

def broker_new(request):
    broker = Broker.objects.all()

    if(broker.count() > 0):
        return redirect('broker_detail')
    else:
        if request.method == "POST":
            form = BrokerForm(request.POST)
            if form.is_valid():
                broker = form.save(commit=False)
                broker.author = request.user
                broker.save()
                return redirect('broker_detail')
        else:
            form = BrokerForm()

    return render(request, 'hyp_app/broker_new.html', {'form': form})


def broker_detail(request): 
    broker = Broker.objects.all()

    if request.method == "POST":
        form = BrokerForm(request.POST, instance=broker[0])
        if form.is_valid():
            broker = form.save(commit=False)
            broker.author = request.user
            broker.save()
            return redirect('broker_detail')
    else:
        form = BrokerForm(instance=broker[0])
    
    return render(request, 'hyp_app/broker_detail.html', {'form': form})

def broker_remove(request):
    print("REMOVER")
    brokers = Broker.objects.all()
    brokers[0].delete()
    print(brokers[0].broker_id)
    return redirect('broker_new')