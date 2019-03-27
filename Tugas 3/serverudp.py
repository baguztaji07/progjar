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

def auto_download():
	tmp = str(data)
	if data == "ijin":
		count=str(count_client)
		#create folder overwrite if already exist
		if os.path.exists('./client'+count):
			shutil.rmtree('./client'+count)
		os.makedirs('./client'+count)
		print "Connected client addr: %s, %s " % addr
		#passing dir for new file
		conn.sendall("client"+count)
		thread = Thread(target=sendImg, args=(conn,))
		thread.start()

def sendImg(tes):
	ngisi = tes
	for x in file_name:
		print "Sending %s ..." % x
		conn.sendall("send")
		#send filename
		conn.sendall(x)
		f = open(x, "rb")
		data = f.read()
		#send img
		conn.sendall(data)
		time.sleep(0.02)
	#check clients
	conn.sendall("fin")
	global count_client
	count_client += 1
	
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(10)
print "Server listening..."
conn, addr = sock.accept()

while True:
	data = conn.recv(1024)
	abc = str(data)
	if (abc=="end"):
		print "Transfer finished\n"
		conn.close()
		#waiting new connection
		print "Server listening..."
		conn, addr = sock.accept()
	auto_download()