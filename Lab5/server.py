import socket
import pandas
server = socket.socket()
print("------------------------------------------")
print("socket is created")
port = 8000
print("socket is binded to port 8000")
server.bind(('', port))
server.listen()
print("server is listening")
print("------------------------------------------")
while True:
    client, address = server.accept()
    print("client is connected")
    print('Server connected to', address)
    client.send(str(pandas.to_datetime("today")).encode())
    print("sending date time to client")
    client.close()
    print("connection for the client is closed")
    print("Waiting for other clients..........")
server.close()