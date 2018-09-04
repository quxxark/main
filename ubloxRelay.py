#!/usr/bin/env python


import serial
import sys
import socket
import select
import time

if len(sys.argv) < 2 or not (sys.argv[1]):
    print('Usage:\nubloxRelay.py <serial port>')
    exit(-1)

isfile = False

try:
    ser = serial.Serial(port=sys.argv[1], timeout=1)
except:
    print('Failed to open serial port ', sys.argv[1])
    # hack: try to open file instead
    try:
        ser = open(sys.argv[1])
        isfile = True
    except:
        exit(-1)



server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind(('', 2222))
except socket.error as msg:
    print(('Bind failed. Error Code : ', str(msg[0]), ' Message ', msg[1]).encode())
    sys.exit()

server_socket.listen(10)

read_list = [server_socket]
client_list = []

while 1:
    
    readable, writable, errored = select.select(read_list, [], [], 0)

    for s in readable:
        if s is server_socket:
            client_socket, address = server_socket.accept()
            client_list.append(client_socket)
            print('Connection from', address)
        else:
            data = s.recv(1024)
            if (data):
                print( 'Data from client:', str(data))
            else:
                print("client connection closed")
                s.close()
                client_list.remove(s)
 
    line = ser.readline()
    output = ''
    if isfile:
        time.sleep(0.1)
        output = line
    else:
        output = line.decode('ASCII')

    output = output.replace('$GN', '$GP')
    print(output)

    for client in client_list:
        client.send(output.encode())

server_socket.close()