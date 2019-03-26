import socket
from threading import Thread
import time
import sys
import os
import shutil

HOST = "127.0.0.1"
PORT = 9000
file_name = ["diandra.jpg", "agatha.jpg", "stewart.jpg", "cynantia.jpg", "bart.png"]
count_client = 1

def req():
	data, addr = sock.recvfrom(1024)
	tmp = str(data)
	if data == "ijin":
		count=str(count_client)
		#create folder
		if os.path.exists('./client'+count):
			shutil.rmtree('./client'+count)
		os.makedirs('./client'+count)
		#passing dir for new file
		sock.sendto("client"+count,addr)
		thread = Thread(target=sendImg, args=(addr))
		thread.start()

def sendImg(ip, port):
	addr = (ip, port)
	for x in file_name:
		print "Sending %s ..." % x
		sock.sendto("send", addr)
		#send filename
		sock.sendto(x,addr)
		f = open(x, "rb")
		data = f.read()
		#send img
		sock.sendto(data, addr)
		time.sleep(0.02)
	#check clients
	print " "
	sock.sendto("fin",addr)
	global count_client
	count_client += 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
	req()