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
data, addr = sock.recvfrom(1024)
sock.sendto(file_name[0], addr)
print "Sending %s ..." % file_name[0]

f = open(file_name[0], "rb")
data = f.read()
ukuran = len(data)

kirim(data,addr)


############
