import socket
from threading import Thread
import time
import sys
import os
import shutil
import glob

HOST = "127.0.0.1"
PORT = 9000
file_name = ["diandra.jpg", "agatha.jpg", "stewart.jpg", "cynantia.jpg", "bart.png"]
count_client = 1
files = glob.glob("*.*")
folder = glob.glob("**/")
basename = "/new_%s"

def list_all():
	for fl in folder:
		conn.sendall(fl)
		ss = conn.recv(1024)
	for fn in files:
		conn.send(fn)
		ss = conn.recv(1024)
	conn.send("finish")

def auto_download():
	#tmp = str(data)
	#if data == "ijin":
	count=str(count_client)
	#create folder overwrite if already exist
	if os.path.exists('./client'+count):
		shutil.rmtree('./client'+count)
	os.makedirs('./client'+count)
	#print "Connected client addr: %s, %s " % addr
	#passing dir for new file
	conn.sendall("client"+count)
	folder.append("client"+count+"/")
	thread = Thread(target=sendImg, args=(conn,))
	thread.start()

def download(uname):
	data = conn.recv(1024)
	if os.path.exists(uname):
		flag = 0
	else :
		os.makedirs(uname)
		folder.append(uname+"/")
	if data in files:
		print "Sending %s ..." % data
		#conn.sendall("send")
		#send filename
		conn.sendall(data)
		f = open(data, "rb")
		data = f.read()
		#send img
		conn.sendall(data)
		time.sleep(0.02)
	#check clients
	conn.sendall("fin")
	print " "

def upload():
	while True:
		filen = sock.recv(1024)
		tmp = str(filen)
		if (tmp=="fin"):
			break
		else:
			f = open(basename % filen, 'wb+')
			#get file
			isi = sock.recv(40960000)
			f.write(isi)
			f.close()
			print "File "+ filen+ " diterima"


def sendImg(tes):
	ngisi = tes
	for fn in files:
		print "Sending %s ..." % fn
		#conn.sendall("send")
		#send filename
		conn.sendall(fn)
		f = open(fn, "rb")
		data = f.read()
		#send img
		conn.sendall(data)
		time.sleep(0.02)
	#check clients
	conn.sendall("fin")
	print " "
	global count_client
	count_client += 1
	
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(10)
# print "Server listening..."
# conn, addr = sock.accept()

while True:
	print "Server listening...\n"
	conn, addr = sock.accept()
	while True:
		cmd = conn.recv(1024)
		abc = str(cmd)
		if (abc=="autodl"):
			auto_download()
			#print "Transfer finished\n"
		if (abc=="ls"):
			list_all()
		if (abc=="dl"):
			conn.sendall("ss")
			data=conn.recv(1024)
			download(data)
		if (abc=="up"):
			thread = Thread(target=upload, args=(conn,))
			thread.start()
		if (abc=="dc"):
			conn.close()
			#count_client += 1
			break
		
	# if (abc=="end"):
	# 	print "Transfer finished\n"
	# 	conn.close()
	# 	#waiting new connection
	# 	print "Server listening..."
	# 	conn, addr = sock.accept()
	#auto_download()