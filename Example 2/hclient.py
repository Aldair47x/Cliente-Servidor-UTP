import zmq
import sys
import time
import socket
import pyaudio
import threading

def rep(s_rep, stream_recv):
	while True:
		msg = s_rep.recv_json()
		info_recv = msg['info']
		stream_recv.write(info_recv.encode('utf-16', 'ignore'))
		s_rep.send_json({'info':'Ok'})
	
def req(s_req, stream_rep, friend, name, CHUNK):
	s_req.send_json({'op':'enter', 'me':name, 'friend':friend})
	s_req.recv_json()
	while True:
		info = stream_rep.read(CHUNK)
		s_req.send_json({'op':'chat', 'me':name, 'friend':friend, 'info':info.decode('utf-16','ignore')})
		s_req.recv_json()

def main():
	if len(sys.argv) != 3:
		print("Error")
		exit()

	ip = sys.argv[1]
	port = sys.argv[2]

	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 0.025
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
	s_req.send_json({'op': 'session', 'name': name, 'ip': "{}:{}".format(my_ip[0],my_ip[1]+1)})
	res = s_req.recv_json()
	print(res['msg'])
	contacts = res['contacts']
	del(contacts[name])

	if res['contacts']:
		print(contacts)
		friend = input("Friend: ")
		print('Calling to {}...'.format(friend))
	else:
		print("There are not friends!")

	context_rep = zmq.Context()
	s_rep = context_rep.socket(zmq.REP)
	s_rep.bind("tcp://*:{}".format(my_ip[1]+1))
	Calling = False

	while True:
		if contacts or Calling:
			Calling = True
			t_req = threading.Thread(target=req, args=(s_req, stream_rep, friend, name, CHUNK,))
			t_req.start()
			t_rep = threading.Thread(target=rep, args=(s_rep, stream_recv,))
			t_rep.start()
			break;
			
		if not Calling:
			msg = s_rep.recv_json()
			friend = msg['friend']
			msg = s_rep.send_json({'info': 'Ok'})
			print('Into to Call...')	
			Calling = True
	print('We are in call !')

if __name__ == '__main__':
	main()
