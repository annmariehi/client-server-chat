# Programming Project 4: Client/Server Chat
# server.py

import socket

def server():
    # SOURCE FOR FOLLOWING SOCKET SET UP:
    # Date: 08/10/22
    # Adapted from function at:
    # URL: https://realpython.com/python-sockets/

    # define host/port/socket
    HOST = socket.gethostname()
    PORT = 3000
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set up socket on server side
    serversocket.bind((HOST, PORT)) # binding host/port
    serversocket.listen() # listening for client
    clientsocket, address = serversocket.accept() # accept connection from client

    # print connection details
    print(f'server listening on: {HOST} on port: {PORT} \nconnected by {address}')
    print('waiting for message...')

    # receive first client message
    recvMessage = clientsocket.recv(1024).decode()

    # if client terminated connection, will receive nothing and close socket
    if not recvMessage:
        print('...client terminated connection.')
        clientsocket.close()

    # print client message
    print(f'c: {recvMessage}')

    # first message prompt
    print('type /q to quit \nenter message to send...')

    # SOURCE FOR FOLLOWING WHILE LOOP:
    # Date: 08/10/22
    # Adapted from function at:
    # URL: https://realpython.com/python-sockets/
    while True:
        message = input('>> ')

        # if user inputs '/q', terminate connection
        if (message == '/q'):
            print('terminating connection...')
            break

        # send the message
        clientsocket.send(message.encode())

        # same as receive first client message
        recvMessage = clientsocket.recv(1024).decode()
        if not recvMessage:
            print('...client terminated connection.')
            break
        print(f'c: {recvMessage}')

    # if broken out of while loop, close connection with client
    clientsocket.close()


if __name__ == '__main__':
    server()
