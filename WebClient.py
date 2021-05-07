from socket import *
serverIP = "localhost"
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
print("Connection is established")
filename = "hello.html"
web = "GET /" + filename + " HTTP/1.1\r\n\r\n"
clientSocket.send(web.encode())
print("sent")

msg = ""
while 1:
    new = clientSocket.recv(2048).decode()
    msg = msg + new
    if (len(new) < 1):
        break
print(msg)
print("connection close")

clientSocket.close()