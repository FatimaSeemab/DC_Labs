import socket
import datetime
from dateutil import parser
from datetime import datetime
def synchronizeTime():
    client = socket.socket()
    port = 5000

    client.connect(('127.0.0.1', port))

    message = (datetime.now())
    print("The time client sending is:",message)
    client.send(str(message).encode())
    while True:
        server_time = (client.recv(1024).decode())
        client_time = (datetime.now())
        # response_time =pandas.to_datetime("today")
        # unsychnronized_time =pandas.to_datetime("today")
        # client_time = server_time + ((response_time-request_time)/2)
        print("The time according to this client should be: ", client_time)
        print("The new time sent by the server node is : ", (server_time))
    # print("The client time before sychronization is:", unsychnronized_time)
    # print("The client time after sychronization is:", client_time)

    # client.close()


# Driver function
if __name__ == '__main__':
    # synchronize time using clock server
    synchronizeTime()