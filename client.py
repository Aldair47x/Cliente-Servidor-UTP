import zmq
import sys

def main():
    if len(sys.argv) != 3:
        print("Error")
        exit()
    ip = sys.argv[1]
    port = sys.argv[2]
    operation = sys.argv[3]

    context = zmq.Context()
    s = context.socket(zmq.REQ)
    s.connect("tcp://{}:{}".format(ip,port))

    if operation == "list":
        s.send_json({"op":"list"})
        files = s.recv_json()
        print(files)
    else:
        print("Error")


    print("Connecting to server {} at {}".format(ip,port))

if __name__ == '__main__':
    main()
