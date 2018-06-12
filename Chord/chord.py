#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import random
import sys
import threading
import zmq
import os
import math
from time import sleep


totalNodes = 32768
powNodes = int(math.log2(totalNodes)) 


class myNode:
	def __init__(self, ip, port, IdHash):
		self.ip = ip
		self.port = port
		self.idhash = IdHash  # Diccionario donde la llave es el id_number del nodo y el valor el socket
		self.hashTable = {} # Diccionario donde la llave es el hash del id_number y el valor una lista de {}
		self.fingertable_ = {} #Un diccionario con llave 2^i-1 + id_number y con valor el nodo asociado
		self.keyvalues_ = [] # Una lista con el intervalo de llaves
		self.successor_ = [] #Una lista con los sucesores del nodo

	def getIp(self):
		return self.ip

	def getPuerto(self):
		return self.port
	
	def setHashT(self,hashT):
		self.hashTable = hashT
		
	def getHashT(self):
		return self.hashTable
		
	def setSuccessor(self,successor):
		self.successor_ = successor
		
	def getSuccessor(self):
		return self.successor_
		
	def setFingerTable(self,fingerTable):
		self.fingertable_ = fingerTable
		
	def getFingerTable(self):
		return self.fingertable_
		
	def setIdHash(self,IdHash):
		self.idhash_ = IdHash
		
	def getIdHash(self):
		return self.idhash_
		
	def setKeyValues(self,keyValues):
		self.keyvalues_ = keyValues
	
	def getKeyValues(self):
		return self.keyvalues_
		
	def toString(self):
		return print(self.getIp()," ",self.getPuerto()," ",self.getIdHash()," ",self.getHashT()," ",self.getSuccessor()," ",self.getFingerTable()," ",self.getKeyValues()," ")
		
	def fingerTable(self):
		for i in range(0,powNodes):
			key = (self.idhash + 2 ** i) % totalNodes
			self.fingertable_[key] = {"id" : self.idhash, "ip": self.ip, "puerto" : self.port, "rangollave" : {"x" :self.keyvalues_[0], "y" : self.keyvalues_[1]}}

	#Recibiendo y actualizando con una nueva finger
	def update_fingerTable(self,table):
		for key in table:
			self.fingertable_[key] = table[key]

	#Imprimir finger Table
	def show_fingerTable(self):
		for key in self.fingertable_:
			print(str(key) +" "+str(self.fingertable_[key]))

	def show_hashTable(self):
		for key in self.hashTable:
			print(str(key) +" "+str(self.hashTable[key]))

#Funcion para verificar si estoy en el rango del nodo
def Check(id_, x, y):
	result = False
	if( x > y):
		if(id_ >= x or id_ <= y):
			result = True

	else:
		if(id_ >= x and id_ <= y):
			result = True

	return result

#Funcion que permite recorrer la finger_table de un nodo y pasarnos los parametros de su sucesor ideal.
def lookupNode(table,id_,op):
	for key in table:
		if(Check(id_,table[key]["rangollave"]["x"],table[llave]["rangollave"]["y"])):
			sgte_id = table[key]["id"]
			sgte_ip = table[key]["ip"]
			sgte_port = table[key]["puerto"]
			if(op==1):
				data={"op" : "siguiente", "id" : sgte_id, "ip": sgte_ip, "puerto": sgte_port}
			else:
				data={"op" : "no_es_llave", "id" : sgte_id, "ip": sgte_ip, "puerto": sgte_port}
			return data

		KeyFinal=key
	#print("No estoy en la finger")
	sgte_id = table[KeyFinal]["id"]
	sgte_ip = table[KeyFinal]["ip"]
	sgte_port = table[KeyFinal]["puerto"]
	#print(str(sgte_id)+"  "+str(sgte_ip)+" "+str(sgte_port))
	if(op==1):
		data={"op" : "siguiente", "id" : sgte_id, "ip": sgte_ip, "puerto": sgte_port}
	else:
		data={"op" : "no_es_llave", "id" : sgte_id, "ip": sgte_ip, "puerto": sgte_port}
	return data

def nextNode(data):
	sgte_id =  data["id"]
	sgte_ip = data["ip"]
	sgte_port = data["puerto"]
	address = "tcp://"+sgte_ip+":"+sgte_port
	return address


#Funcion que se ejecuta en el hilo que queda esperando el ingreso de un mensaje
def Server(canal_servidor, port, mi_nodo,contexto):
	canal_servidor.bind("tcp://*:"+port)

	while True:
		mensaje = canal_servidor.recv_json()
		#condicional por medio del cual el nodo entrante busca su puesto en el chord
		if (mensaje["op"] == "conexion"):
			print("\n")
			print("Se esta conectado a mi el nodo "+str(mensaje["id"]))
			entrada_nodo_id = mensaje["id"]
			aqui_es = Check(entrada_nodo_id, mi_nodo.getKeyValues()[0], mi_nodo.getKeyValues()[1])
			#Si el nodo entrante esta en el rango de llaves del nodo de ingreso.
			if(aqui_es):
				data={"op": "si", "x":mi_nodo.getKeyValues()[0] , "y":entrada_nodo_id}
				mi_nodo.setKeyValues([((entrada_nodo_id+1) % totalNodes),((mi_nodo.getIdHash())% totalNodes)])
				print("Rango: "+str(mi_nodo.getKeyValues()[0]) +" - "+ str(mi_nodo.getKeyValues()[1]))	
			else:
				print("Lo siento, te comunico con un nodo sucesor.")
				table = mi_nodo.getFingerTable()
				data=lookupNode(table,entrada_nodo_id,1)
			canal_servidor.send_json(data)
		#Pasando los archivos al nuevo nodo que se conecta
		elif (mensaje["op"] == "roteme_partes"):
			archivos = mi_nodo.getHashT()
			archivos_to_send ={}
			if not archivos:
				print("Diccionario de archivos vacios, nada para enviar")
				canal_servidor.send_json({"op": "nada_para_enviar"})
			else:
				for llave in archivos:
					if(Check(llave,mensaje["mi_x"], mi_nodo.getKeyValues()[0]-1)):
						print("Llave a rotar: "+str(llave))
						archivos_to_send[llave] = archivos[llave]
				canal_servidor.send_json({"op" : "rotando_partes", "lista_partes": archivos_to_send})
				canal_servidor.recv_string()
				print("Archivos a enviar: ")
				print(archivos_to_send)

				for llavesita in archivos_to_send:
					with open(archivos_to_send[llavesita], "rb") as entrada:
						print(llavesita)
						info = entrada.read()
						canal_servidor.send(info)
						canal_servidor.recv_string()
						os.remove(archivos_to_send[llavesita])
						del archivos[llavesita]
				canal_servidor.send_string("Terminamos")

		elif(mensaje["op"] == "pasandote_partes"):
			mis_archivos = mi_nodo.getHashT()
			archivos_to_recv = mensaje["partes"]
			canal_servidor.send_string("mandame_partes")
			if not archivos_to_recv:
				print("Ningun archivo para recibir")
			else:
				for key in archivos_to_recv:
					mis_archivos[key] = archivos_to_recv[key]
					with open(archivos_to_recv[key], "ab+") as entrada:
						print(key)
						info = canal_servidor.recv() 
						entrada.write(info)
						entrada.close()
						canal_servidor.send_string("siga")
				print("Transferencia de archivos por SALIDA del nodo exitosa")
		#Condicional que nos permite actualizar la finger table del nodo que esta ingresando.
		elif(mensaje["op"] == "actualizando"):
			#print("Actualizando Inicio  --- Actualizando finger del nuevo")
			#mi_nodo.show_Finger()
			llave_check = mensaje["llave"]
			#print(llave_check)
			if(Check(llave_check, mi_nodo.getKeyValues()[0], mi_nodo.getKeyValues()[1])):
				#print("SI estoy")
				msj = {"op": "es_llave", "id": mi_nodo.getIdHash(), "ip": mi_nodo.getIp() , "puerto": mi_nodo.getPuerto(), "rx" :mi_nodo.getKeyValues()[0], "ry" : mi_nodo.getKeyValues()[1]}
			else:
				my_finger = mi_nodo.getFingerTable()
				msj=lookupNode(my_finger,llave_check,2)
			canal_servidor.send_json(msj)
			#print("Actualizando Fin")
		#Condicional que ejecuta la orden de actualizacion de las finger tables.
		elif(mensaje["op"] == "rueda_la_bola"):
			#Actualizando Finger
			finger = mi_nodo.getFingerTable()
			for key in finger:
				if(Check(key, mensaje["rx"], mensaje["ry"])):
					finger[key]["id"] = mensaje["id"]
					finger[key]["ip"] = mensaje["ip"]
					finger[key]["puerto"] = mensaje["puerto"]
					finger[key]["rangollave"]={"x": mensaje["rx"],"y":mensaje["ry"]}

			canal_servidor.send_string("Listo")
			print("Rodando la bola")
			mi_nodo.update_Finger(finger)
			mi_nodo.show_Finger()			

			if(mensaje["start"] != finger[(mi_nodo.getIdHash() + 2 ** 0) % totalNodes]["id"]):
				socket_sucesor = contexto.socket(zmq.REQ)
				key_sucesor = (mi_nodo.getIdHash() + 2**0) % totalNodes
				ip_sucesor = finger[key_sucesor]["ip"]
				puerto_sucesor = finger[key_sucesor]["puerto"]
				dir_sucesor = "tcp://"+ip_sucesor+":"+puerto_sucesor
				solicitud = {"op": "rueda_la_bola" , "id": mensaje["id"], "rx": mensaje["rx"], "ry": mensaje["ry"],"rxi":mensaje["rxi"], "ryi": mensaje["ryi"],"ip": mensaje["ip"], "puerto": mensaje["puerto"], "start": mensaje["start"]}
				socket_sucesor.connect(dir_sucesor)
				socket_sucesor.send_json(solicitud)
				socket_sucesor.disconnect(dir_sucesor)

		elif(mensaje["op"] == "Eliminar_nodo"):
			if(mensaje["stop"]):
				l = mi_nodo.getKeyValues()
				l[0] = mensaje["rxi"]
				mi_nodo.setKeyValues(l)
			print("Rango: "+str(mi_nodo.getKeyValues()[0]) +" - "+ str(mi_nodo.getKeyValues()[1]))
			finger = mi_nodo.getFingerTable()
			for key in finger:
				if(Check(key, mensaje["rxi"], mensaje["ryi"])):
					finger[key]["id"] = mensaje["id"]
					finger[key]["ip"] = mensaje["ip"]
					finger[key]["puerto"] = mensaje["puerto"]
					finger[key]["rangollave"]={"x": mensaje["rxi"],"y":mensaje["ryi"]}

			canal_servidor.send_string("Listo")
			print("Eliminar_nodo")
			mi_nodo.update_Finger(finger)
			mi_nodo.show_Finger()	
			socket_sucesor = contexto.socket(zmq.REQ)
			key_sucesor = (mi_nodo.getIdHash() + 2**0) % totalNodes
			id_sucesor = finger[key_sucesor]["id"]
			ip_sucesor = finger[key_sucesor]["ip"]
			puerto_sucesor = finger[key_sucesor]["puerto"]		
			print(key_sucesor)
			print(mensaje["start"])
			if(key_sucesor != mensaje["start"]):
				dir_sucesor = "tcp://"+ip_sucesor+":"+puerto_sucesor				
				solicitud = {"op": "Eliminar_nodo" , "id": mensaje["id"], "rxi": mensaje["rxi"], "ryi": mensaje["ryi"],"ip": mensaje["ip"], "puerto": mensaje["puerto"], "start": mensaje["start"],"stop":False}
				socket_sucesor.connect(dir_sucesor)
				socket_sucesor.send_json(solicitud)
				socket_sucesor.disconnect(dir_sucesor)

		elif(mensaje["op"]=="cargar_parte"):
			if(Check(mensaje["llave"], mi_nodo.getKeyValues()[0], mi_nodo.getKeyValues()[1])):
				mensaje = {"op":"enviela"}
				canal_servidor.send_json(mensaje)

			else:
				table = mi_nodo.getFingerTable()
				data=lookupNode(table,mensaje["llave"],1)
				canal_servidor.send_json(data)

		elif(mensaje["op"] == "enviando_parte"):

			key = mensaje["llave"]
			archivo = mensaje["nombre_archivo"]
			parte = mensaje["parte"]
			canal_servidor.send_string("Listo")
			info_parte = canal_servidor.recv()
			canal_servidor.send_string("fin")
			mis_archivos = mi_nodo.getHashT()
			mis_archivos[key] = archivo+parte
			with open(archivo+parte,"ab+") as output:
				output.write(info_parte)
			mi_nodo.setHashT(mis_archivos)
			mi_nodo.show_hashTable()

		elif(mensaje["op"] == "solicito_parte"):
			if(Check(int(mensaje["llave"]), mi_nodo.getKeyValues()[0], mi_nodo.getKeyValues()[1])):
				data_parte = open(mensaje["parte"],"rb")
				info_parte = data_parte.read()
				mensaje = {"op":"recibela"}
				canal_servidor.send_json(mensaje)
				canal_servidor.recv_string()
				canal_servidor.send(info_parte)

			else:
				table = mi_nodo.getFingerTable()
				data=lookupNode(table,int(mensaje["llave"]),1)
				canal_servidor.send_json(data)

	
def main():
	#Solo para el ingreso del primer nodo del chord.
	if(len(sys.argv) == 3):
		my_ip = sys.argv[1]
		my_port = sys.argv[2]
		ide = random.randrange(0,totalNodes-1)
		#ide=int(input("Id : "))
		print(ide)
		nuevo = myNode(my_ip, my_port,ide)
		comp_x = ide + 1
		comp_y = ide
		l = [comp_x,comp_y]
		nuevo.setKeyValues(l)
		

		nuevo.fingerTable()
		conectado = True
	#Se ejecuta del segundo nodo en adelante
	if(len(sys.argv) == 5):
		my_ip = sys.argv[1]
		my_port = sys.argv[2]
		ide = random.randrange(0,totalNodes-1)
		#ide=int(input("Id : "))
		print(ide)
		print("\n")
		nuevo = myNode(my_ip, my_port,ide)
		nuevo.fingerTable()

		other_ip = sys.argv[3]
		other_port = sys.argv[4]

		address = "tcp://"+other_ip+":"+other_port
		conectado = False

	#Se crea el contexto y se ejecuta el hilo de escucha.
	context= zmq.Context()
	socket_cliente = context.socket(zmq.REQ)
	socket_servidor = context.socket(zmq.REP)
	thread_server = threading.Thread(target=Server, args=(socket_servidor, my_port, nuevo, context))
	thread_server.start()

	#Ciclo para conectar nodo
	while not conectado:

		socket_cliente.connect(address)

		data = {"op" : "conexion","id" : nuevo.getIdHash(), "ip" : nuevo.getIp(), "puerto" : nuevo.getPuerto()}
		socket_cliente.send_json(data)
		respuesta = socket_cliente.recv_json()

		#Condicional ejecutada despues de saber donde se debe conectar el nodo.
		if(respuesta["op"] == "si"):
			print(respuesta["op"])
			nuevo.SetX(respuesta["x"])
			nuevo.SetY(respuesta["y"])
			print("Rango: "+str(nuevo.getKeyValues()[0]) +" -- "+ str(nuevo.getKeyValues()[1])+"\n")
			#Actualizando Finger
			new_finger = {}
			for i in range(0,powNodes):
				encontrado = False
				llave = (nuevo.getIdHash() + 2 ** i) % totalNodes
				#print(llave)
				
				if(Check(llave,nuevo.getKeyValues()[0],nuevo.getKeyValues()[1])):
					new_finger[llave] = {"id" : nuevo.getIdHash(), "ip": nuevo.getIp() , "puerto" : nuevo.getPuerto(), "rangollave" : {"x" :nuevo.getKeyValues()[0], "y" : nuevo.getKeyValues()[1]}}
					#print("Me pertenece esta llave")
				else:
					#Llenado de finger table
					while not encontrado:
						socket_cliente.send_json({"op": "actualizando", "llave": llave})
						#print(llave)
						mensaje = socket_cliente.recv_json()
						#print(mensaje)
						if (mensaje["op"] == "es_llave"):
							new_finger[llave] = {"id" : mensaje["id"], "ip": mensaje["ip"] , "puerto" : mensaje["puerto"], "rangollave" : {"x" :mensaje["rx"], "y" :mensaje["ry"]}}
							encontrado=True
						elif (mensaje["op"] == "no_es_llave"):
							sgte_ip = mensaje["ip"]
							sgte_port = mensaje["puerto"]
							socket_cliente.disconnect(address)
							address = "tcp://"+sgte_ip+":"+sgte_port
							socket_cliente.connect(address)
			nuevo.update_Finger(new_finger)
			print("\n")
			print("He Actualizado mi finger con exito"+"\n")
			nuevo.show_Finger()
			conectado=True

		#Condicion que se ejecuta cuando se necesita conectar al nodo siguiente de una finger_table de un nodo conocido
		elif(respuesta["op"] == "siguiente"):
			socket_cliente.disconnect(address)
			address = nextNode(messajepuesta)
		#Si el nodo se encuentra conectado, y su fingerTable actualizada 
		if(conectado):
			sucesor_finger = nuevo.getFingerTable()
			key_sucesor = (nuevo.getIdHash() + 2 ** 0) % totalNodes
			xsucesor=sucesor_finger[key_sucesor]["rangollave"]["x"]
			ysucesor=sucesor_finger[key_sucesor]["rangollave"]["y"]

			sucesor={"id": sucesor_finger[key_sucesor]["id"], "ip": sucesor_finger[key_sucesor]["ip"], "puerto": sucesor_finger[key_sucesor]["puerto"]}
			solicitud = {"op": "rueda_la_bola" , "id": nuevo.getIdHash(), "rx": nuevo.getKeyValues()[0], "ry": nuevo.getKeyValues()[1],"rxi":xsucesor , "ryi": ysucesor, "ip": nuevo.getIp(), "puerto": nuevo.getPuerto(), "start": nuevo.getIdHash()}
			socket_cliente.disconnect(address)
			address = "tcp://"+sucesor["ip"]+":"+sucesor["puerto"]
			socket_cliente.connect(address)
			socket_cliente.send_json(solicitud)
			socket_cliente.recv_string()

			#Recibiendo los archivos que me corresponden
			print("Empezando a rotar archivos...")

			solicitud_partes = {"op": "roteme_partes","mi_x":nuevo.getKeyValues()[0]}
			socket_cliente.send_json(solicitud_partes)
			responde = socket_cliente.recv_json()

			if(responde["op"] == "rotando_partes"):
				partes = responde["lista_partes"]
				socket_cliente.send_string("Mandelas")
				print("Partes Recibidas son: ")
				print(partes)
				for llave in partes:
					with open(partes[llave], "ab+") as entrada:
						print("Recibiendo info parte..."+llave)
						info = socket_cliente.recv()
						socket_cliente.send_string("Siga")
						entrada.write(info)
						entrada.close()
				socket_cliente.recv_string()
			elif(responde["op"] ==  "nada_para_enviar"):
				print("No hay archivos para recibir")

	while conectado:
		print("\t" + "******<<<<<<<<<<<<<<<<<<<<<<Menu Chord>>>>>>>>>>>>>>>>>>>>>******")
		print("\n")
		print("1) Cargar archivo en el Chord")
		print("\n")
		
		op=int(input("(?): "))

		if(op==1):
			filename = input("Filename: ")
			extension =  "." + input("Extension del archivo sin el . ")

			resultados = open(filename+".txt","ab+")

			with open(filename+extension, "rb") as entrada:
				data = entrada.read()
				tam = entrada.tell()
				lim=tam/(1024*1024)
				print("Size>> "+ str(tam))
				parts=int(lim+1)
				i=0
				print ("# >>: "+ str(parts))
				entrada.seek(0)
				archivos_nuevos = nuevo.getHashT()
				while i<=lim:
					enviado = False
					key = random.randrange(0,totalNodes-1)
					to_write = str(key)+"-"+filename+str(i+1)+extension+"\n"
					resultados.write(to_write.encode('utf-8'))
					print("ID generado para la parte>> "+str(key))					

					if(Check(key,nuevo.getKeyValues()[0],nuevo.getKeyValues()[1])):
						archivos_nuevos[key] = filename+str(i+1)+extension
						data_part=entrada.read(1024*1024)
						with open(filename+str(i+1)+extension,"ab+") as output:	
							output.write(data_part)
					else:
						data={"op": "cargar_parte", "llave": key}

						while not enviado:				
							
							socket_cliente.send_json(data) 
							msj=socket_cliente.recv_json()
							if(msj["op"] == "enviela"):
								data_part=entrada.read(1024*1024)
								msj={"op" : "enviando_parte", "nombre_archivo":filename,"parte":str(i+1)+str(extension),"llave":key}
								socket_cliente.send_json(msj)

								socket_cliente.recv_string()
								socket_cliente.send(data_part)
								socket_cliente.recv_string()
								enviado = True
								print("Enviado con exito")

							elif(msj["op"] == "siguiente"):
								socket_cliente.disconnect(address)
								address = nextNode(messaje)
								socket_cliente.connect(address)
						print("Enviada")		
					i+=1
				nuevo.setHashT(archivos_nuevos)
			nuevo.show_hashTable()
			resultados.close()
			print("Partes enviadas")


		


main()
