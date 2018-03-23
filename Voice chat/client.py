import zmq
import sys
import socket
import pyaudio
import threading

def rep(s_rep, stream_recv):
	while True:
		msg = s_rep.recv_json()
		stream_recv.write(msg['info'].encode('utf-16', 'ignore'))
		s_rep.send_json({'info':'Ok'})

def req(s_req, stream_rep, name, room, CHUNK):
	while True:
		info = stream_rep.read(CHUNK)
		s_req.send_json({'op':'chat', 'name': name, 'room': room, 'info':info.decode('utf-16','ignore')})
		s_req.recv_json()

def menu(s_req, name):
	while True:
		print('...Chat Rooms...')
		print('1. Show rooms availables')
		print('2. Enter a room ')
		print('3. Create your room')
		print('4. Salir')
		op = input('Option: ')
		print('\n')
		if op == '1':
			s_req.send_json({'op': 'list'})
			res = s_req.recv_json()
			if res['chat_rooms']:
				print(res['chat_rooms'])
			else:
				print('There are not chat rooms.')
			print('\n')
		if op == '2':
			number_room = input('Number chat room: ')
			room = 'room {}'.format(number_room)
			break
		if op == '3':
			s_req.send_json({'op': 'create', 'person': name})
			res = s_req.recv_json()
			room = res['room']
			break
		if op == '4':
			print('Bye...')
			exit()
	return room

def main():
	if len(sys.argv) != 3:
		print("Error")
		exit()

	ip = sys.argv[1]
	port = sys.argv[2]

	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	audio = pyaudio.PyAudio()
	stream_rep = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	stream_recv = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

	name = input("Name: ")
	get_my_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	get_my_ip.connect(("gmail.com",80)) 
	my_ip = get_my_ip.getsockname()

	context_req = zmq.Context()
	s_req = context_req.socket(zmq.REQ)
	s_req.connect("tcp://{}:{}".format(ip,port))

	print(my_ip, my_ip[1]+1)
	s_req.send_json({'op': 'session', 'name': name, 'ip': '{}:{}'.format(my_ip[0],my_ip[1]+1)})
	res = s_req.recv_json()

	context_rep = zmq.Context()
	s_rep = context_rep.socket(zmq.REP)
	s_rep.bind("tcp://*:{}".format(my_ip[1]+1))

	room = menu(s_req, name)
	print('You are in {} now'.format(room))

	t_req = threading.Thread(target=req, args=(s_req, stream_rep, name,room, CHUNK))
	t_req.start()
	t_rep = threading.Thread(target=rep, args=(s_rep, stream_recv))
	t_rep.start()



if __name__ == '__main__':
	main()
