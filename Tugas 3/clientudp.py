import socket
import select
import time
import sys
import os

HOST = "127.0.0.1"
PORT = 9000
server_addr = ('127.0.0.1',9000)
basename = "/new_%s"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)
sock.send("ijin")
#dirpath for new file
count = sock.recv(1024)
while True:
	tmp = sock.recv(1024)
	if tmp == "fin":
		break
	if tmp == ('send'):
		#get filename
		data = sock.recv(1024)
		f = open(count + basename % data, 'wb+')
		#get file
		isi = sock.recv(40960000)
		f.write(isi)
		f.close()
		print "File "+ data+ " diterima"

sock.send("end")		
sock.close()