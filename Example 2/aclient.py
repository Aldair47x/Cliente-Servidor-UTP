import zmq
import sys
import socket
import pyaudio
import threading

def menu(s_req, name):
	print('1. Directory ')
	print('2. Call')
	while True:
		op = input('Option: ')
		if op == 1:
			s_req.send_json({'op':'list'})
			res = s_req.recv_json()
			conctacts = res['contacts']
			del(contacts[name])
			if res['contacts']:
				print(contacts)
			else:
				print("There are not friends!")
		if op == 2:
			friend = input('Friend: ')
			print('Calling to {}...'.format(friend))
			s_req.send_json({'op':'Enter', 'friend':friend})
			res = s_req.recv_json()
			if res['op'] == False:
				print('Rejected call... Sorry !')
			else :
				print('Connected call')
				break
	return Friend
	
def rep(s_rep):
	

def req(s_req, name):
	s_req.send_json({'op': 'session', 'name': name, 'ip': "{}:{}".format(my_ip[0],my_ip[1]+1)})
	res = s_req.recv_json()
	friend = menu(s_req, name)
	while True:



def rep(s_rep):
	

def main():
	global Calling
	global Friend
	Calling = False
	if len(sys.argv) != 3:
	print("Error")
	exit()

	ip = sys.argv[1]
	port = sys.argv[2]

	name = input("Name: ")
	get_my_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	get_my_ip.connect(("gmail.com",80)) 
	my_ip = get_my_ip.getsockname()

	context_req = zmq.Context()
	s_req = context_req.socket(zmq.REQ)
	s_req.connect("tcp://{}:{}".format(ip,port))
	t_req = threading.Thread(tarjet=req, args=(s_req, name,))
	t_req.start()
	
	context_rep = zmq.Context()
	s_rep = context_rep.socket(zmq.REP)
	s_rep.bind("tcp://*:{}".format(my_ip[1]+1))
	t_rep = threading.Thread(tarjet=req, args=(s_req, name,))
	t_rep.start()



