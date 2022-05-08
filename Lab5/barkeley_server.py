import socket
from dateutil import parser

import datetime

clients={}

def create_master_node():
    server=socket.socket()
    ip_address="127.0.0.1"
    port=5000
    server.bind((ip_address,port))
    server.listen(5)
    print("master nose is waiting for the clients.......")
    connect_slaves(server)
def connect_slaves(server):
    while True:
        client, address = server.accept()
        print("client is connected")
        message = parser.parse(client.recv(512).decode())
        server_time = datetime.datetime.now()

        clock_difference = server_time.timestamp() - message.timestamp()

        print("time from the client", address, "is", message)
        print("The clock difference between server and client is: ", clock_difference)
        clients[address] = {
            "client": client,
            "time": message,
            "clock_difference": clock_difference
        }
        synchronize_time()

def average():
    difference=[]
    for value in clients.values():
        print()
        difference.append(value["clock_difference"])
    if len(clients)>1:
        Sum=sum(difference)
        average=Sum/len(clients)
        print("average time difference is:",average)
        return average
    else:

        return difference[0]

def synchronize_time():
    print("Number of clients to be synchronized: " + str(len(clients)))
    
    if len(clients) > 0:
        average_clock_difference = average()
        for client_addr, client in clients.items():
            time = datetime.datetime.now()
            synchronized_time = time.timestamp() + average_clock_difference
            synchronized_time = datetime.datetime.fromtimestamp(synchronized_time)
            print("synchronized time is:", synchronized_time)
            client['client'].send(str(synchronized_time).encode())
        print("data sent...")
    else:
        print("No client data.")
    print("-------------------------------------------------------")

create_master_node()
