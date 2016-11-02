import socket

SERVER = "10.62.0.148"	#IP adress of server node
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#create socket
s.connect((SERVER, 8000))	#connect to server at port 8000
s.send("GET " + "/echo.php?message=myMessage" + " HTTP/1.0\r\nHost: " + SERVER + "\r\n\r\n") #Send a get message to server
data = s.recv(1024) #recieve echo and response
print (data)