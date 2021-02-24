#!/usr/bin/python3
import socket, time


host = input("Enter the current IP: ")  # Add the server IP manually
# host = ""  # Hardcode of the server IP
# host = socket.gethostbyname(socket.gethostname())  # Add the server IP automatically
port = 9090
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("[INFO: Server Started]")

while True:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)

        message_time = time.strftime("%d-%m-%Y-%H.%M.%S", time.localtime())

        print("["+addr[0]+"]=["+str(addr[1])+"]=["+message_time+"]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print("\n[INFO: Server Stopped]")
        break

s.close()
