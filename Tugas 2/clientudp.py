import socket
import select
import time
import sys

HOST = "127.0.0.1"
PORT = 5005
buf = 1024
timeout = 3
basename = "new_%s"

#########
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(basename, (HOST, PORT))


data, addr = sock.recvfrom(1024)
if data:
	print "File diterima:", data
	file_name = data.strip()

f = open(basename % file_name, 'wb')
while True:
	ready = select.select([sock], [], [], timeout)
	if ready[0]:
		data, addr = sock.recvfrom(40960000)
		f.write(data)
	else:
		print "Finish!"
		f.close()
		break
sock.close()
###########