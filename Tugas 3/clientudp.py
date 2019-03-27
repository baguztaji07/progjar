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
#sock.send("ijin")
#dirpath for new file
#count = sock.recv(1024)
uname = raw_input('Name: ')
while True:
	command = raw_input('Ur command: ')
	if command == "exit":
		sock.send("dc")
		break
	# if command == "ls":
	# 	sock.send(ls)
	if command == "list_all":
		sock.send("ls")
		while True:
			fold = sock.recv(1024)
			tmp = str(fold)
			if (tmp=="finish"):
				break
			sock.send("ss")
			print tmp

	if command == "download":
		sock.send("dl")
		ss = sock.recv(1024)
		sock.sendall(uname)
		command = raw_input('Filename: ')
		sock.sendall(command)
		while True:
			filen = sock.recv(1024)
			tmp = str(filen)
			if (tmp=="fin"):
				break
			else:
				f = open(uname+"/" + basename % filen, 'wb+')
				#get file
				isi = sock.recv(40960000)
				f.write(isi)
				f.close()
				print "File "+ filen+ " diterima"

	if command == "auto_download":
		#dfn = raw_input('Filename: ')
		sock.send("autodl")
		count = sock.recv(1024)
		while True:
			filen = sock.recv(1024)
			tmp = str(filen)
			if (tmp=="fin"):
				break
			else:
				f = open(count + basename % filen, 'wb+')
				#get file
				isi = sock.recv(40960000)
				f.write(isi)
				f.close()
				print "File "+ filen+ " diterima"

	#tmp = sock.recv(1024)
	# if tmp == "fin":
	# 	break
	# # if tmp == ('send'):
	# 	#get filename
	# 	data = sock.recv(1024)
	# 	f = open(count + basename % data, 'wb+')
	# 	#get file
	# 	isi = sock.recv(40960000)
	# 	f.write(isi)
	# 	f.close()
	# 	print "File "+ data+ " diterima"

#sock.send("end")		
sock.close()