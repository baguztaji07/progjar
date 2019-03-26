import socket
import select
import time
import sys
import os

HOST = "127.0.0.1"
PORT = 9000
basename = "/new_%s"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("ijin", (HOST, PORT))
#dirpath for new file
count, addr = sock.recvfrom(1024)
while True:
	tmp, addr = sock.recvfrom(1024)
	if tmp == "fin":
		break
	if tmp == ('send'):
		#get filename
		data, addr = sock.recvfrom(1024)
		f = open(count + basename % data, 'wb+')
		#get file
		isi, addr = sock.recvfrom(40960000)
		f.write(isi)
		f.close()
		print "File "+ data+ " diterima"
		
sock.close()