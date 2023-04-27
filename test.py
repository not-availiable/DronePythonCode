import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host=socket.gethostname()
host='192.168.1.89'
port=12000
s.connect((host,port))
#fileToSend = open("ToSend.txt","r")
#content = fileToSend.read()
while True:
	fileToSend = open("ToSend.txt","r")
	content = fileToSend.read()
	s.send(content.encode())
	msg=""
	try:
		msg=s.recv(10000)
	except:
		print("noMsg")

	if msg:
		msg = msg.decode('utf-8')
		print(msg)
