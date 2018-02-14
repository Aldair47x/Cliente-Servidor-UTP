import zmq
import sys
import time

def main():
    if len(sys.argv) != 4:
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
    elif operation == "download":
        name = input("Name of song: ")
        s.send_json({"op":"download", "file":name})
        parts = s.recv_json()
        start = time.time()
        for i in range(int(parts["parts"])):
            s.send_json({"op":"download", "file":name, "part":"{}".format(i)})
            file = s.recv()
            with open("download {}".format(name) , "ab") as output:
                output.write(file)
        end = time.time()
        print("Download Success in {} seconds!".format(end - start))
    else:
        print("Error")


    print("Connecting to server {} at {}".format(ip,port))

if __name__ == '__main__':
    main()
