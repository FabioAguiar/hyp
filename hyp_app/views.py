from django.shortcuts import render, get_object_or_404
from .models import User, Login, Peripheral, Cycle, Broker
from .forms import PeripheralForm, CycleForm, BrokerForm, LoginForm, UserForm
from django.shortcuts import redirect
from datetime import datetime
from . import mqtt, config_helper
import time
from base64 import b64encode, b64decode
import ast

import pyrebase
from django.contrib import auth


config = config_helper.configFirebase()

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


def firebase_data(peripheral):
    data = {"Name": peripheral.name, 
        "Technical Name": peripheral.technical_name,
        "Topic Base": peripheral.name,
        "Type Peripheral": peripheral.type_peripheral,
        "Topic Name": peripheral.topic_name,
        "Specification": peripheral.specification,
        "Description": peripheral.description,
        "Topic MQTT": peripheral.name,
        "Is activated": peripheral.is_activated,
        "Is activated": peripheral.is_activated,
        "Data Metric": peripheral.data_metric                 
    }
    return data

def user_firebase(uid):
    user = b64decode(uid).decode("utf-8")
    user = b64decode(user)
    user = ast.literal_eval(user.decode('utf-8'))
    try:
        userF = auth.sign_in_with_email_and_password(user['email'], user['passwd'])
    except:
        message="invalid credentials"
        #return render(request,'hyp_app/user_new.html',{'messg':message})

    return userF

def userId(email, passwd):
    data = {"email": email, "passwd": passwd}
    data = str.encode(str(data))
    data = b64encode(data)
    uid = b64encode(data).decode("utf-8")
    return uid


def signIn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            passwd = request.POST.get('passwd')

            uid = userId(email,  passwd)

            try:
                user = auth.sign_in_with_email_and_password(email, passwd)
            except:
                message="invalid credentials"
                return render(request,'hyp_app/login.html',{'messg':message})

            peripherals = Peripheral.objects.all()

            request.session['uid']=uid
            print(uid)
            return render(request, 'hyp_app/dashboard.html', {'peripherals': peripherals})
    else:
        form = LoginForm()
    
    return render(request, 'hyp_app/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return render(request,'hyp_app/login.html')


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            try:
                auth.create_user_with_email_and_password(user.email, user.passwd)
                userF = auth.sign_in_with_email_and_password(user.email, user.passwd)
            except:
                message="invalid credentials"
                return render(request,'hyp_app/user_new.html',{'messg':message})


            data = {"email": user.email, "passwd": user.passwd}
            data = str.encode(str(data))
            data = b64encode(data)
            uid = b64encode(data).decode("utf-8")

            email = {"email": user.email}
            db.child("users").child(uid).set(email, userF['idToken'])
            request.session['uid']=uid
            peripherals = Peripheral.objects.all()

            return render(request, 'hyp_app/dashboard.html', {'peripherals': peripherals})
    else:
        form = UserForm()
        
    return render(request, 'hyp_app/user_new.html', {'form': form})


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

def peripheral_firebase_id():
    strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    strnow = str.encode(str(strnow))
    return b64encode(strnow).decode("utf-8")

def peripheral_new(request):
    print(request.session['uid'])
    if request.method == "POST":
        form = PeripheralForm(request.POST)
        if form.is_valid():

            peripheral = form.save(commit=False)
            peripheral.author = request.user
            peripheral.firebase_id = peripheral_firebase_id()
            peripheral.save()

            data = firebase_data(peripheral)
            user = user_firebase(request.session['uid'])
            db.child("users").child(request.session['uid']).child('device').child(peripheral.type_peripheral).child(peripheral.firebase_id).update(data, user['idToken'])

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

            user = user_firebase(request.session['uid'])       
            data = firebase_data(peripheral)
            uid = request.session['uid']

            db.child("users").child(request.session['uid']).child('device').child(peripheral.type_peripheral).child(peripheral.firebase_id).update(data, user['idToken'])
            #dados = db.child("users").child(uid).child('device').child(peripheral.type_peripheral).child(peripheral.firebase_id).get(userF['idToken'])
            #print(dados.val())

            return redirect('peripheral_detail', pk=peripheral.pk)
    else:
        form = PeripheralForm(instance=peripheral)
        form.pk = pk

    return render(request, 'hyp_app/peripheral_detail.html', {'form': form})    

def peripheral_remove(request, pk):
    peripheral = get_object_or_404(Peripheral, pk=pk)    
    user = user_firebase(request.session['uid'])
    db.child("users").child(request.session['uid']).child('device').child(peripheral.type_peripheral).child(peripheral.firebase_id).remove(user['idToken'])
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