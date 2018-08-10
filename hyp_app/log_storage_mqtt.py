import sqlite3
import time

dbFile = "db.sqlite3"


def writeToDb(timeDate, timeHour, topic, payload):
	conn = sqlite3.connect(dbFile)
	c = conn.cursor()
	aux = topic[:-4]

	# lendo os dados
	c.execute("""
	SELECT topic_path, topic_name FROM hyp_app_topics WHERE topic_path LIKE '""" + aux + """%';
	""")
	#Separa o nome do topico da busca realizada
	name = c.fetchone()[1]
	#Trata o valor capturado pelos sensores, retirando os caracteres 'b', '[' e ']' da String	
	value = payload[2:-1]
	#Separa a referencia do sensor que ocupa os dois ultimos caracteres do topico
	reference = topic[len(aux)+2:]
	#Inserção dos valores na base
	print ("Writing to db...")
	c.execute("INSERT INTO hyp_app_mqttlog (name,value,reference, timeDate, timeHour) VALUES (?,?,?,?,?)", ( name, value, reference, timeDate, timeHour))			
	conn.commit()	
	conn.close()
	#return