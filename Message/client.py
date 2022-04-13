# Python program to implement client side of chat room.
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


IP_address = "127.0.0.1"
Port = 5050

server.connect((IP_address, Port))

while True:

    # maintains a list of possible input streams
    socket_list = [socket.socket(), server]

    ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)

    for sock in ready_to_read:
        if sock == server:
            message = sock.recv(2048)
            print(message)
        else:
            message=str(input())
            server.send(message)

server.close()
