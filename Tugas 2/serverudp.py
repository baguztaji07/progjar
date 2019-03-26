import socket
import select
import time
import sys

HOST = "127.0.0.1"
PORT = 5005
file_name = ["di.jpg", "dia.jpg", "stew.jpg", "cynan.jpg", "bart.png"]

def kirim(isi,address):
    while (isi):
        if(sock.sendto(isi, address)):
            isi = f.read()
            time.sleep(0.02) # Give receiver a bit time to save


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

#########
for x in file_name:
	data, addr = sock.recvfrom(1024)
	sock.sendto(x, addr)
	print "Sending %s ..." % x

	f = open(x, "rb")
	data = f.read()
	#ukuran = len(data)

	kirim(data,addr)
	#print "selesai"
data = sock.recvfrom(1024)
sock.sendto("fin", addr)

############
