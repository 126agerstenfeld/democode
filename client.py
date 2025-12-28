import socket

serverIP = input("Enter the Server's IP address: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverIP, 12345))

message = input("Enter message to send here: ")
client.send(message.encode())

client.close()
