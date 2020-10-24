#!/usr/bin/python3

import socket
import threading
import time

key = 8194

shutdown = False
join = False


def receiving(name, sock):
    while not shutdown:  # Workaround. With 'True' value is not working
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0
server_ip = input("Enter the server IP: ")  # strongly recommended to hardcode the server-IP value
server = (server_ip, 9090)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()


while shutdown == False:
    if join == False:
        s.sendto(("["+alias + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input('>>> ')

            if message != "":
                s.sendto(("["+alias + "] :: "+message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("["+alias + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
