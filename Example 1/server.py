import zmq
import sys
import os
import math

def loadFiles(path):
    files = {}
    dataDir = os.fsencode(path)
    for file in os.listdir(dataDir):
        filename = os.fsdecode(file)
        print("Loading {}".format(filename))
        files[filename] = file
    return files

def main():

    if len(sys.argv) != 3:
        print("Error")
        exit()

    directory = sys.argv[2]
    port = sys.argv[1]

    context = zmq.Context()
    s = context.socket(zmq.REP)
    s.bind("tcp://*:{}".format(port))
    files = loadFiles(directory)

    while True:
        msg = s.recv_json()
        if msg["op"] == "list":
            s.send_json({"files": list(files.keys())})
        elif msg["op"] == "download":
            size = 1024*1024
            filename = msg["file"]
            if filename in files:
                if not "part" in msg:
                    file = os.stat(directory + "/" +filename)
                    s.send_json({"parts": math.ceil(file[6]/size)})
                else:
                    with open(directory + "/" +filename, "rb") as input:
                        print(msg["part"])
                        input.seek(size * int(msg["part"]))
                        data = input.read(size)
                    s.send(data)
            else:
                s.send_string("Song does not exits! Marranito")
        else:
            print("Unsupported action!")

if __name__ == '__main__':
    main()

