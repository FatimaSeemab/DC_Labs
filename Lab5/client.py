import socket
import pandas
from dateutil import parser

def synchronizeTime():
    s = socket.socket()
    port = 8000

    s.connect(('127.0.0.1', port))
    request_time = pandas.to_datetime("today")
    server_time = parser.parse(s.recv(1024).decode())
    response_time =pandas.to_datetime("today")
    unsychnronized_time =pandas.to_datetime("today")
    client_time = server_time + ((response_time-request_time)/2)
    print("The travel time between client and server is: ",((response_time-request_time)/2))
    print("The client time before sychronization is:", unsychnronized_time)
    print("The client time after sychronization is:", client_time)

    # s.close()


# Driver function
if __name__ == '__main__':
    # synchronize time using clock server
    synchronizeTime()