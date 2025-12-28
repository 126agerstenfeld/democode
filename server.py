import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0", 12345))
server.listen(1)

print("Waiting for connection")
connection, address = server.accept()
print("Connected by", address)

message = connection.recv(1024).decode()
print("Message received from client:", message)

connection.close()
