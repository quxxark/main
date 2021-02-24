#!/usr/bin/python3
import socket, threading, time


SHUTDOWN = False
JOIN = False
CLIENT_TIMEOUT = 0.2


def receiving(sock):
    while not SHUTDOWN:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(CLIENT_TIMEOUT)
        except:
            print('Something went wrong')


host = socket.gethostbyname(socket.gethostname())
port = 0
server_ip = input("Enter the server IP: ")  # strongly recommended to hardcode the server-IP value
server = (server_ip, 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(False)

username = input("Name: ")

rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()


while SHUTDOWN is False:
    if JOIN is False:
        s.sendto(("["+username+"] => join chat").encode("utf-8"), server)
        JOIN = True
    else:
        try:
            message = input('>>> ')

            if message != "":
                s.sendto(("["+username+"] :: "+message).encode("utf-8"), server)
            time.sleep(CLIENT_TIMEOUT)
        except:
            s.sendto(("["+username+"] <= left chat ").encode("utf-8"), server)
            SHUTDOWN = True

rT.join()
s.close()
