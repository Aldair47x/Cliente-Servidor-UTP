import zmq
import sys
import os
import math
import threading 

def main():
	if len(sys.argv) != 2:
		print("Error")
		exit()

	port = sys.argv[1]
	contacts = {}
	inCalling = {}
	#192.168.8.217
	context = zmq.Context()
	s_rep = context.socket(zmq.REP)
	s_rep.bind("tcp://*:{}".format(port))
	
	context_req = zmq.Context()
	s_req = context_req.socket(zmq.REQ)

	while True:    	
		msg = s_rep.recv_json()
		if msg['op'] == 'session':
			contacts[msg['name']] = msg['ip']
			inCalling[msg['name']] = msg['ip']
			print("{} {}".format(msg['name'], msg['ip']))
			s_rep.send_json({'msg':'Established connection', 'contacts': contacts})
		if msg['op'] == 'list':
			s_rep.send_json({'contacts': contacts})
		if msg['op'] == 'chat':
			s_rep.send_json({'info':'Ok'})
			friend = msg['friend']
			info = msg['info']		
			me = msg['me']
			#input()
			#print("Friend: {}\ninfo: {}\nme: {}\n".format(friend, info, me))
			s_req.connect("tcp://{}".format(inCalling[friend]))
			s_req.send_json({'friend':me,'me':friend, 'info':info})
			s_req.recv_json()
			if friend in contacts:
				del(contacts[friend])
			if me in contacts:
				del(contacts[me])

if __name__ == '__main__':
	main()
