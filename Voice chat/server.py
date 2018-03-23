import zmq
import sys
import os
import math

def main():
	if len(sys.argv) != 2:
		print("Error")
		exit()

	port = sys.argv[1]
	contacts = {}
	chat_rooms = {}
	room = 0
	context = zmq.Context()
	s_rep = context.socket(zmq.REP)
	s_rep.bind("tcp://*:{}".format(port))
	
	context_req = zmq.Context()
	s_req = context_req.socket(zmq.REQ)
	print('Server is running...')
	while True:    	
		msg = s_rep.recv_json()
		if msg['op'] == 'session':
			contacts[msg['name']] = msg['ip']
			print("{} {}".format(msg['name'], msg['ip']))
			s_rep.send_json({'msg':'Ok'})
		if msg['op'] == 'list':
			s_rep.send_json({'chat_rooms': list(chat_rooms.keys())})
		if msg['op'] == 'create':
			name_room = 'room {}'.format(room)
			chat_rooms[name_room] = []
			chat_rooms[name_room].append(msg['person'])
			s_rep.send_json({'room': name_room})
			room+=1
		if msg['op'] == 'chat':
			s_rep.send_json({'info': 'Ok'})
			for person in chat_rooms[msg['room']]:
				if person != msg['name']:
					s_req.connect("tcp://{}".format(contacts[person]))
					s_req.send_json({'info': msg['info']})
					s_req.recv_json()

if __name__ == '__main__':
	main()
