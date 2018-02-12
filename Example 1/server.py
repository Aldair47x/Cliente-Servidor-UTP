import zmq
import sys
import os

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
    filesparts = {}

    while True:
        msg = s.recv_json()
        if msg["op"] == "list":
            s.send_json({"files": list(files.keys())})
        elif msg["op"] == "download":
            size = 1024*1024
            filename = msg["file"]
            if not filename in filesparts:
                parts = []
                if filename in files:
                    with open(directory + "/" +filename, "rb") as input:
                        data = input.read(size)
                        parts.append(data)
                        while data:
                            data = input.read(size)
                            parts.append(data)
                    print(filename)
                    filesparts[filename] = parts
                    s.send_json({"parts":len(parts)})
                else:
                    s.send_string("Marranito")
            else:
                s.send(filesparts[filename][int(msg["part"])])
        else:
            print("Unsupported action!")

if __name__ == '__main__':
    main()
