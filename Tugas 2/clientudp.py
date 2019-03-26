import socket
import time
import sys

HOST = "127.0.0.1"
PORT = 5005
buf = 1024
# file_name = sys.argv[1]
file_name = "di.jpg"
file_name1 = "dia.jpg"
file_name2 = "stew.jpg"
file_name3 = "cynan.jpg"
file_name4 = "bart.png"

konter=1
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(file_name, (HOST, PORT))
print "Sending %s ..." % file_name

f = open(file_name, "rb")
data = f.read()
ukuran = len(data)


while(data):
    if(sock.sendto(data, (HOST, PORT))):
        data = f.read()
        print konter
        time.sleep(0.02) # Give receiver a bit time to save
    konter = konter + 1

sock.close()
f.close()