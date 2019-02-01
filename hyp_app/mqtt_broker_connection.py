from time import gmtime, strftime
from . import log_storage_mqtt
import paho.mqtt.client as mqtt
import sys

#definicoes: 
Broker = "m14.cloudmqtt.com"
PortaBroker = 14167
KeepAliveBroker = 60
TopicoSubscribe = "grow/#" #dica: troque o nome do topico por algo "unico", 
                                    #Dessa maneira, ninguem ira saber seu topico de
                                    #subscribe e interferir em seus testes

#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))

    #faz subscribe automatico no topico
    client.subscribe(TopicoSubscribe)

#Callback - mensagem recebida do broker
def on_message(client, userdata, msg):
    dateTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    hourTime = strftime("%H:%M:%S", gmtime())    
	#result = (theTime + "\t" + str(msg.payload))
    print("[MSG RECEBIDA] Topic: "+msg.topic+" / Mensagem: "+str(msg.payload)+"Time: "+theTime)
    log_storage_mqtt.writeToDb(dateTime, hourTime, msg.topic, str(msg.payload))



#programa principal:
try:
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        #client.on_publish = on_publish
        #client.on_subscribe = on_subscribe  

        client.username_pw_set('cxhovvsp', 'v-nT9GcH_-Cr')


        client.connect(Broker, PortaBroker, KeepAliveBroker)
except KeyboardInterrupt:
        print(" pressionado, encerrando aplicacao e saindo...")
        sys.exit(0)