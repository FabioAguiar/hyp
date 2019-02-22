import sqlite3
import time

dbFile = "db.sqlite3"
topico = ""
valor = 0;

def writeToDb(topic, value):
	conn = sqlite3.connect(dbFile)
	c = conn.cursor()


	#print("Topico: " + topic)
	#print("Valor: " + value)


	# lendo os dados
	c.execute("""
	SELECT mqtt_topic FROM hyp_app_peripheral WHERE mqtt_topic == '""" + topic + """';
	""")


	for mqtt_topic in c:
		topico = mqtt_topic[0]
		aux = value[2:-1]
		valor = str(float(aux))
	


	c.execute("""
	UPDATE hyp_app_peripheral SET last_record_state = """ + valor + """ WHERE mqtt_topic == '""" + topic + """';
	""")
	#print(mqtt_topic[0])
	#print(valor)
	
	conn.commit()	
	conn.close()

	
	#Separa o nome do topico da busca realizada
	#name = c.fetchone()[1]
	
	#Trata o valor capturado pelos sensores, retirando os caracteres 'b', '[' e ']' da String	
	#value = payload[2:-1]
	
	#Separa a referencia do sensor que ocupa os dois ultimos caracteres do topico
	#reference = topic[len(aux)+2:]
	
	#Inserção dos valores na base
	#print ("Writing to db...")
	#c.execute("INSERT INTO hyp_app_mqttlog (name,value,reference) VALUES (?,?,?)", ( name, value, reference))			
	#conn.commit()	
	#conn.close()
	#return